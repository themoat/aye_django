#So basically I am trying to create a user profile automatically as soon as the user signs up, so for that
#to automatically happen, we use signals.
#So below we see, basically importing post_save from signals. Then importing User and Profile, so we know whose
#profile has been created. Then finally for that signal to be caught up, use a receiver, and use it as a decorator


from django.db.models.signals import post_save
from .models import User,Profile
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


#Now when create profile function is done, fully let's also create a save profile function.

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()



#Finally let's add into our apps.py file in the same users application only.

