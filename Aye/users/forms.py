from django import forms
from .models import User,Profile

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Unique username',max_length=50,help_text='Required! Please enter a unique username')
    phone = forms.IntegerField()


    class Meta:
        model = User
        fields = ('phone','username','first_name','last_name')

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField()

    class Meta:
        model = User
        fields = ('username','last_name')

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField()
    class Meta:
        model = Profile
        fields = ('image','bio')