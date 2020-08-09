from rest_framework import status
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer,UserSerializer,UserProfileSerializer
from ..models import User,Profile,send_otp_via_sms,generate_otp
from twilio.rest import Client


twilio_client = Client()


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserRegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class UserLoginView(APIView):

#     #Since it has been just inheriting from base APIView, we basically have to create our own methods.
#     #And Ofcourse the views are gonna use permissison classes, so we mention that below.
#     #So basically any sort of method, whether it's get, put , post , we have to define it here.


#     permission_classes = [AllowAny]
#     serializer_class = UserLoginSerializer

#     # So i am just defining post method. And remember post method here is not similar to CreateAPIView
#     # since post method is used just once to post something, and nothing gets saved, while this is not the case
#     # with CreateAPIView.


#     #we basically arent saving anything, we just get the data from the respective serializer and do stuff with that.


#     def post(self,request,*args,**kwargs):
#         # So we basically get the data in form of request.data just like the way we did with django forms
#         # using request.POST//// We are basically gonna play with serializer data only.

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             new_data = serializer.data
#             return Response(new_data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class UserProfileView(APIView):
    #Since we already put default permission class as AuthenticatedorReadOnly, so we don't need this permission class here
    # permission_classes = [IsAuthenticated,]
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()

    def get(self,request, *args, **kwargs):
        user = get_object_or_404(User, username=kwargs['username'])
        profile_serializer = UserProfileSerializer(user.profile)
        return Response(profile_serializer.data)


    def create(self,request,*args,**kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Gotta understand how to do this clearly.

# class ProfileUpdateView(APIView):
#     permission_classes = [AllowAny,]
#     serializer_class = UserProfileSerializer
#     queryset = Profile.objects.all()
#
#
#     def post(self,request,*args,**kwargs):
#         serializer = UserProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileViewset(viewsets.ModelViewSet):
    model = Profile
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = []







class LogoutView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



#for resending otp also.
@api_view(['GET'])
def send_otp(request, phone):
    try:
        user = User.objects.get(phone=phone)

        send_otp_via_sms(phone, user.otp)

        return Response(status=200)
    except User.DoesNotExist:
        return Response(status=404)

"""How do I make url's for both of these. Is the existing way that I did is ryt or not."""



@api_view(['GET'])
def validate_otp_code(request, otp_code, phone):
    try:
        user = User.objects.get(otp=otp_code, phone=phone)
        user.is_active = True
        user.otp = generate_otp()
        user.save()
        return Response({'success': True})
    except User.DoesNotExist:
        return Response(status=404)
    return Response(None, None)

