from django.contrib import admin

from .models import Happening,Upcomingclubs,ExternalEvents
# Register your models here.

class HappeningAdmin(admin.ModelAdmin):
    list_display = ('name','time','link')
    search_fields = ('name',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Happening,HappeningAdmin)
admin.site.register(Upcomingclubs)
admin.site.register(ExternalEvents)

