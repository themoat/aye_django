#These serializers will be responsible for serializing/unserializing  the User model into and out of various formats.

from rest_framework import serializers
from ..models import User,Profile, generate_otp, send_otp_via_sms
from twilio.rest import Client
from rest_framework.response import Response
twilio_client = Client()



class UserSerializer(serializers.ModelSerializer):

    # used for displaying list of users, with serializing the fields as written.

    class Meta:
        model = User
        fields = ('username','first_name','last_name')



"""Check this below UserProfileSerializer, if I have implemented the right custom methods."""

class UserProfileSerializer(serializers.ModelSerializer):

    #in this profile serialzier when user displys basically wanna see the user whose profile it is , so we
    # make use of the UserSerializer by mentioning it here.
    #Also we don't want anyone to change this user, so mention read_only as True,

    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields=('user','bio','image')


    def update(self,instance,validated_data,*args,**kwargs):
        user_data = validated_data.pop('user',{})
        user = instance.user
        instance.bio = validated_data.get('bio',instance.bio)
        instance.image = validated_data.get('image',instance.image)
        instance.save(*args,**kwargs)
        return instance




class UserRegistrationSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields=[
            'username',
            'first_name',
            'last_name',
            'profile',
            'phone'

        ]

    # So here I am gonna override the create method, so I am  basically changing what create method is
    # I can use this create method on any ModelSerializer, I am just using it, for creating user.

    def create(self, validated_data):
    # so basically we validate the data entered in the fields we use for creating a new user.

        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        phone = validated_data['phone']

    # we basically get all the validated data which was entered, so we finally create the user object.

        profile_data = validated_data.pop('profile')
        user_obj = User(**validated_data)

        user_obj.otp = generate_otp()
        send_otp_via_sms(user_obj.phone, user_obj.otp)

        user_obj.save()

        profile = Profile.objects.create(user=user_obj,**profile_data)

        return user_obj    #is the return statement right here



    # Here now I am going to write validate method, which is basically going to find out whether the data(not validated_data)
    # that has been entered, already exists or not. If it does, it will give Validation error.


    def validate(self, data):
        phone = data['phone']
        username = data['username']

        user_qs = User.objects.filter(phone=phone)
        user_qs2 = User.objects.filter(username=username)
        if user_qs.exists() or user_qs2.exists():
            raise serializers.ValidationError("Both your phone number and username entered must be unique, looks like these already exist")

        return data


"""Is this right login serializer, considering where are we taking user's input for otp"""
class UserLoginSerializer(serializers.ModelSerializer):

    # Here we basically try to login the user through phone and OTP, and after entering both, a token is generated
    #which we finally use to authenticate ourselves.

    #Here we over-ride the fields, since we want them to look and gather data the way we want them to.

    phone = serializers.IntegerField()
    token = serializers.CharField(max_length = 255,allow_blank=True,read_only=True)

    class Meta:
        model = User
        fields = ('phone','token')

    # According to this above what we wrote in this serializer we try to wrap this up in,a view.
    # so checkout the UserLoginView.
    #Now we need to validate this data, as in if this correct or not, so we will do that.
    #So here I need ot able to do either authenticate the user with their phone and stuff.
    #So we do that here below.

    def validate(self, data):
        user_obj = None
        phone = data.get('phone', None)
        #here we see that what's the phone data that user enters.
        if not phone:
            raise serializers.ValidationError("Phone number is required to login")
        #now we filter to find our user objects related for phone

        user = User.objects.get(phone=phone)

        if user is None:
            raise serializers.ValidationError(
                'A user with this phone number is not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        # if user.exists() and user.count == 1:
        #     user = user.first()

        return user and user.username

        # data['token'] = "SOME RANDOM TOKEN"
        # return data






