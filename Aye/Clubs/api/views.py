#This is where we hold our api views to display data.
from rest_framework.generics import ListAPIView,RetrieveAPIView
from ..models import clubs,Rooms
from .serializers import ClubSerializer,ClubDetailSerializer,RoomSerializer

class ClubsListAPIView(ListAPIView):
    queryset = clubs.objects.all()
    serializer_class = ClubSerializer


class ClubsDetailAPIView(RetrieveAPIView):
    queryset = clubs.objects.all()
    serializer_class = ClubDetailSerializer

class FemaleRoomsListAPIView(ListAPIView):
    queryset = Rooms.objects.filter(club_name=1)
    serializer_class = RoomSerializer

class MaleRoomsListAPIView(ListAPIView):
    queryset = Rooms.objects.filter(club_name=2)
    serializer_class = RoomSerializer
