from django.urls import path
from .views import HappeningListAPIView,UpcomingclubsListAPIView,ExternalEventsListAPIView
urlpatterns=[

    path('',HappeningListAPIView.as_view(),name='happening-list'),

    path('upcoming_clubs',UpcomingclubsListAPIView.as_view(),name='upcoming-clubs'),

    path('external_events',ExternalEventsListAPIView.as_view(),name='external-events'),

]


