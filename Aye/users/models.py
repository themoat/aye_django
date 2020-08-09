from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from PIL import Image
import os
import random
import string
from rest_framework import status
from rest_framework.response import Response
from twilio.rest import Client
twilio_client = Client()
# Create your models here.

#Since we are creating our own custom user model, I gotta have to put all the fields that I did put to avoid errors.
# Also we are creating certain functions that just have to be created/used in a custom Django User model, so just C/P.
#them.

#Also we make sure that our migrations file in users app, is empty in the beginning, since this is our
# first custom user model being created.

def generate_otp(length=6):
    val = random.randint(123456, 789238)
    return val



def send_otp_via_sms(number,code):


    message = twilio_client.messages.create(to = f"{number}",from_=os.getenv('TWILIO_NUMBER'),body=f"~ ~Yippie! We made it over the international ~waters~,your <aye> OTP is {code}")
    return Response(status=status.HTTP_200_OK)






# So in this I am gonna write methods to define what happens when a normal user is created and what happens when a
#superuser is created.

class MyAccountManager(BaseUserManager):

    def create_user(self,phone,username,first_name,last_name):
        if not phone:
            raise ValueError("Users must have a valid phone number")
        if not username:
            raise ValueError("Users must have a valid username")
        if not first_name:
            raise ValueError("Users must have a valid First Name")
        if not last_name:
            raise ValueError("Users must have a valid last name")


        user = self.model(
            phone=phone,
            username=username,
            first_name=first_name,
            last_name=last_name

        )

        user.save(using=self._db)
        return user

    def create_superuser(self,username,phone,first_name,last_name,password = None):
        user = self.create_user(
               username=username,
               phone=phone,
               first_name=first_name,
               last_name=last_name,
        )
        user.set_password(password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    phone = models.CharField(unique=True,max_length=20)
    username = models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    otp = models.CharField(max_length=10,default='')


    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username','first_name','last_name']


    objects = MyAccountManager()



    def __str__(self):
        return self.username


    def has_perm(self,perm,obj = None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

# Now we need to write a custom User Manager Model, as per Django Docs,which we did above.


#Finally at last we got to the settings.py file and add a small property that we need to for this custom User model.

# Now we want to create a user profile model, so we will do that.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    bio = models.CharField(max_length=140,blank=True)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'


    #will do, once we use aws lambda function let's leave it for now.

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img = Image.open(self.image.path)
    #
    #     if img.height>300 or img.width>300:
    #         output_size=(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    #Here i overwrite the save method, by writing it again.

