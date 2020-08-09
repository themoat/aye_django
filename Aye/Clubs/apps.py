# This is our apps configuration,from which we take the name ClubsConfig and put in our settings.py installed apps.
# This is a necessary thing to do, cause django will have to look for templates automatically, and also needed,for models

from django.apps import AppConfig

class ClubsConfig(AppConfig):
    name = 'Clubs'
