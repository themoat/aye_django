from django.contrib.auth.backends import BaseBackend
from users.models import User


class OTPBackend(BaseBackend):
    def authenticate(self, request, phone=None, password=None):
        try:
            return User.objects.get(phone=phone, otp=password)
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None