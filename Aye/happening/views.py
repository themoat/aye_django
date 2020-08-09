from django.shortcuts import render,redirect
from users.models import User
from .models import Happening

# Create your views here.

def home(request):
    if 'phone' in request.session:
        phone = request.session['phone']

        context = {
            'happenings':Happening.objects.all(),

        }
        return render(request,template_name='happening/happening_home.html', context=context)
    else:
        return redirect('login')

