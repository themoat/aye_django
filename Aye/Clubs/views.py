from django.shortcuts import render,redirect
from .models import clubs,Rooms
from users.models import User
from rest_framework.decorators import authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Create your views here.
# In the below function, we use render, and context is taken to pass information into our html templates,from backend.


#I am creating a dictionary in my home function.

def home(request):
    if 'phone' in request.session:
        phone = request.session['phone']
        user1 = User.objects.get(phone=phone)

        context = {
            'clubs':clubs.objects.all(),
            'user':user1

        }
        return render(request,template_name='Clubs/home.html', context=context)
    else:
        return redirect('login')


def room_female(request):
    if 'phone' in request.session:
        phone = request.session['phone']
        user1 = User.objects.get(phone=phone)

        context={


            'rooms':Rooms.objects.filter(club_name='1'),
            'clubs':clubs.objects.get(name='alpha-f'),
        }
        return render(request,template_name='Clubs/rooms.html',context=context)
    else:
        return redirect('login')

def room_male(request):
    if 'phone' in request.session:
        phone = request.session['phone']
        user1 = User.objects.get(phone=phone)

        context={

            'rooms':Rooms.objects.filter(club_name='2'),
            'clubs':clubs.objects.get(name='alpha-m'),
        }

        return render(request,template_name='Clubs/rooms.html',context=context)

    else:
        return redirect('login')
