from django.urls import path
from .views import UserRegistrationView,UserListView,UserProfileView,LogoutView
from . import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile-update', views.ProfileViewset)  #this works fine

urlpatterns=[

    path('register/', UserRegistrationView.as_view(), name='user-create'),  #this works fine
    # path('login/', UserLoginView.as_view(), name='user-login'),  #we have a different code for this.
    path('list/', UserListView.as_view(), name='user-list'),        #this works fine
    path('profile/<str:username>', UserProfileView.as_view(), name='user-profile'),     #this works fine
    # path('profile_update/<int:pk>',ProfileUpdateView.as_view(),name='profile-update'),
    path('logout/', LogoutView.as_view(), name='user-logout'),   #not needed i think so

    path('send_otp/<str:phone>', views.send_otp, name='send-otp'),  #this works fine
    path('validate_otp_code/<int:otp_code>/<str:phone>', views.validate_otp_code, name='validate-otp-code'),  #works fine
] +router.urls






