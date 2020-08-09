"""Aye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import sys
sys.path.append("..")

# from ..users.views import register,validate,login,logout_view

from users import views as user_views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubs/',include('Clubs.urls')),
    path('happening/',include('happening.urls')),
    path('register/',user_views.register,name = 'register'),
    # path('validate/',user_views.validate_otp,name = 'validate_otp'),
    # path('validate_login',user_views.validate_login_otp,name = 'validate_login_otp'),
    # path('login/',user_views.login, name='login'),
    # path('logout/',user_views.logout_view,name='logout'),
    # path('resend/',user_views.resend_otp,name='resend'),
    # path('resend_register',user_views.resend_register,name='resend_register'),
    path('profile/',user_views.profile,name='profile'),
    path('api/clubs/',include('Clubs.api.urls'),name='clubs-api'),
    path('api/happening/',include('happening.api.urls'),name='happening-api'),
    path('api/auth/token/',TokenObtainPairView.as_view(),name='token-obtain-pair'),
    path('api/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/users/',include('users.api.urls')),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
