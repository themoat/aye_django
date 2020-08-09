from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.

class Happening(models.Model):
    name = models.CharField(max_length = 120)
    description = models.CharField(max_length=140,blank=True)
    photo = models.ImageField(default='',upload_to='happening_images')
    time = models.TextField(max_length=50,blank=True)
    link = models.URLField(max_length=50,blank=True)


    def __str__(self):
        return self.name


    # will use aws labda later to enable it.

    # def save(self):
    #     super().save()
    #     img1=Image.open(self.photo.path)
    #
    #     if img1.width>300 or img1.height>300:
    #         output_size = (900,600)
    #         img1.thumbnail(output_size)
    #         img1.save(self.photo.path)

class Upcomingclubs(models.Model):
    name = models.CharField(max_length=80)
    wall_pic = models.ImageField(default='',upload_to='upcoming_clubs_images')


    def __str__(self):
        return self.name


    #will use aws lambda later to enable it.

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img2=Image.open(self.wall_pic.path)
    #
    #     if img2.width>500 or img2.height>500:
    #         output_size = (900,900)
    #         img2.thumbnail(output_size)
    #         img2.save(self.wall_pic.path)


class ExternalEvents(models.Model):
    name = models.CharField(max_length = 60)
    main_pic = models.ImageField(default='',upload_to='external_events_images')
    time = models.TextField(max_length=50,blank=True)
    link = models.URLField(max_length=50,blank=True)

    def __str__(self):
        return self.name



    #I am commenting this resizing thing in the backend, cause it doesn't function well with AWS S3, so if we later want
    #to use this, we will have to use AWS Lambda function for that, so let's leave that for now.


    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img3 = Image.open(self.main_pic.path)
    #
    #     if img3.width>300 or img3.height>300:
    #         output_size = (900,600)
    #         img3.thumbnail(output_size)
    #         img3.save(self.main_pic.path)
    #
