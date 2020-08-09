from rest_framework.generics import ListAPIView
from ..models import Happening,Upcomingclubs,ExternalEvents
from .serializers import HappeningSerializer,UpcomingclubSerializer,ExternalEventSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class HappeningListAPIView(ListAPIView):
    queryset = Happening.objects.all()
    serializer_class = HappeningSerializer



class UpcomingclubsListAPIView(ListAPIView):
    queryset = Upcomingclubs.objects.all()
    serializer_class = UpcomingclubSerializer


class ExternalEventsListAPIView(ListAPIView):
    queryset = ExternalEvents.objects.all()
    serializer_class = ExternalEventSerializer
