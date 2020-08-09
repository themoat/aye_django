from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('username','first_name','last_name','phone','last_login','is_admin','is_staff')
    search_fields = ('username','first_name','phone')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User,AccountAdmin)
admin.site.register(Profile)



