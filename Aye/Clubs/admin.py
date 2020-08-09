from django.contrib import admin
from .models import clubs,Rooms

# Regsiter your models here.

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('room_name','club_name')
    search_fields = ('room_name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()




admin.site.register(clubs)
admin.site.register(Rooms,RoomsAdmin)


