from rest_framework.serializers import ModelSerializer

from happening.models import Happening, Upcomingclubs,ExternalEvents

class HappeningSerializer(ModelSerializer):
    class Meta:
        model = Happening
        fields=['name',
                'description',
                'photo',
                'time',
                'link',

                ]


class UpcomingclubSerializer(ModelSerializer):
    class Meta:
        model = Upcomingclubs
        fields=[

            'name',
            'wall_pic',

        ]

class ExternalEventSerializer(ModelSerializer):
    class Meta:
        model = ExternalEvents
        fields=[

            'name',
            'main_pic',
            'time',
            'link',

        ]