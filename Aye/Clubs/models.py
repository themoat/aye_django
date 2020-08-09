from django.db import models
from django.conf import settings
from django.utils import timezone
from PIL import Image
# Create your models here.
# Each class is going to be its own table in the database.

class clubs(models.Model):
    name = models.CharField(max_length=150)
    tagline = models.TextField(max_length=300, default=None)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    content_picture = models.ImageField(default='', upload_to='club_images')
    profile_picture = models.ImageField(default='', upload_to='club_images')
    wall_picture = models.ImageField(default='', upload_to='club_images')
    rooms_total = models.IntegerField()

    def __str__(self):
        return self.name


    #will implement this once we use aws lambda function later on, so let's leave it for now.


    # def save(self):
    #     super().save()
    #     img1 = Image.open(self.content_picture.path)
    #     img2 = Image.open(self.profile_picture.path)
    #     img3 = Image.open(self.wall_picture.path)
    #
    #     if img1.height > 300 or img2.height>300 or img3.height > 300 or img1.width > 300 or img2.width > 300 or img3.width > 300:
    #         output_size = (900,600)
    #         output_display_size = (300,300)
    #         img1.thumbnail(output_size)
    #         img2.thumbnail(output_display_size)
    #         img3.thumbnail(output_size)
    #         img1.save(self.content_picture.path)
    #         img2.save(self.profile_picture.path)
    #         img3.save(self.wall_picture.path)



class Rooms(models.Model):
    room_name = models.CharField(max_length=150)
    club_name = models.ForeignKey(clubs,on_delete=models.CASCADE)

    def __str__(self):
        return self.room_name





