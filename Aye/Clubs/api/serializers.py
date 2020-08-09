from rest_framework.serializers import ModelSerializer
from ..models import clubs,Rooms

class ClubSerializer(ModelSerializer):

    class Meta:
        model = clubs
        fields=['id',
                'name',
                'tagline',
                'date_created',
                'profile_picture',
                'rooms_total',
                'url'
                ]

class ClubDetailSerializer(ModelSerializer):

    class Meta:
        model = clubs
        fields=[
            'name',
            'tagline',
            'content',
            'date_created',
            'content_picture',
            'profile_picture',
            'wall_picture',
            'rooms_total',
        ]

class RoomSerializer(ModelSerializer):

    class Meta:
        model = Rooms
        fields=[
            'room_name',
            'club_name',
        ]

