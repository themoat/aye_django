from django.shortcuts import render,redirect
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
import os
from twilio.rest import Client
from django.contrib import messages
from .models import User
import requests
# Create your views here.

twilio_client = Client()

generateotp_url = 'https://api.generateotp.com/'

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            request.session['phone']=phone
            request.session['username']=username
            request.session['first_name']=first_name
            request.session['last_name']=last_name
            otp_code = make_otp_request(phone)

            if otp_code:
                send_otp_code(phone,otp_code)
                messages.info(request,f"Your OTP Code has been generated")
                return redirect('validate_otp')
            else:
                messages.error("Something went wrong, could not generate OTP, please retry.")

            return redirect('validate_otp')

    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def send_otp_via_sms(number,code):
    message = twilio_client.messages.create(to = f"+91{number}",from_=os.getenv('TWILIO_NUMBER'),body = f"~~ ~~ Yippie!! We made it over the waters, your OTP is {code}")


def make_otp_request(phone):
    r = requests.post(f"{generateotp_url}/generate", data={'initiator_id':phone})

    if r.status_code == 201:
        data = r.json()
        otp_code = str(data['code'])
        return otp_code


def send_otp_code(phone,otp_code):
    return send_otp_via_sms(phone,otp_code)


def verify_otp_code(otp_code,phone):
    r = requests.post(f"{generateotp_url}/validate/{otp_code}/{phone}")
    if r.status_code == 200:
        data = r.json()
        status = data['status']
        message = data['message']
        return status, message
    return None, None



def validate_otp(request):
    phone=request.session['phone']
    username=request.session['username']
    first_name=request.session['first_name']
    last_name=request.session['last_name']


    if request.method =='GET':
        return render(request,'users/validate.html')
    otp_code = request.POST['otp_code']
    error = None
    if not otp_code:
        messages.error("A valid otp code is required.")
        return render(request,'users/validate.html')
    if request.session['phone']==phone:
        status,message = verify_otp_code(otp_code,phone)
        if status is True:
            request.user = User(phone=phone,username=username,first_name=first_name,last_name=last_name)
            request.user.save()
            del request.session['first_name']
            del request.session['last_name']
            messages.success(request,f"~~ Welcome to the club, your are in.")
            return redirect('clubs-home')
        elif status is False:
            messages.error(request,f"Something went wrong, please retry, you will soon join the club")
            return redirect('validate_otp')
    return redirect('register')


def login(request):
    if request.method=='GET':
        if 'phone' in request.session:
            return redirect('clubs-home')
        else:
            return render(request,'users/login.html')

    elif request.method =='POST':
        phone = request.POST['phone']
        user = User.objects.filter(phone=phone)
        if user is not None:
            otp_code = make_otp_request(phone)

            if otp_code:
                send_otp_code(phone, otp_code)
                messages.info(request, f"Your OTP Code has been generated")
                request.session['phone'] = phone
                return redirect('validate_login_otp')
            else:
                messages.error("Something went wrong, could not generate OTP, please retry.")

            return redirect('validate_login_otp')

        else:
            return redirect('register')

    else:
        return render(request,'users/register.html')


def logout_view(request):
    phone = request.session['phone']
    try:
        del request.session['phone']
    except KeyError:
        pass
    messages.success(request,"You are successfully logged out, but we are sad to see you go away. ")
    return redirect('login')


def resend_otp(request):
    phone = request.session['phone']

    if request.method =='GET':
        otp_code = make_otp_request(phone)
        if otp_code:
            send_otp_code(phone,otp_code)
            return redirect('validate_login_otp')


def resend_register(request):
    phone = request.session['phone']

    if request.method=='GET':
        otp_code = make_otp_request(phone)
        if otp_code:
            send_otp_code(phone,otp_code)
            return redirect('validate_otp')



def validate_login_otp(request):
    phone = request.session['phone']

    if request.method == 'GET':
        return render(request, 'users/validate_login.html')
    otp_code = request.POST.get('otp_code')
    error = None
    if not otp_code:
        messages.error("A valid otp code is required.")
        return render(request, 'users/validate_login.html')
    if request.session['phone'] == phone:
        status, message = verify_otp_code(otp_code, phone)
        if status is True:
            messages.success(request, f"~~ Welcome to the club, your are in.")
            return redirect('clubs-home')
        elif status is False:
            messages.error(request, f"Something went wrong, please retry, you will soon join the club")
            return redirect('validate_login_otp')
    return redirect('login')


def profile(request):
    if request.method =='GET':
        if 'phone'in request.session:
            phone = request.session['phone']
            user1 = User.objects.get(phone=phone)
            u_form = UserUpdateForm(instance=user1)
            p_form = ProfileUpdateForm(instance=user1.profile)

        else:
            messages.error(request, f"Please, You gotta login first hacker!")
            return redirect('login')

    elif request.method == 'POST':
        if'phone' in request.session:
            phone = request.session['phone']
            user1 = User.objects.get(phone=phone)
            u_form = UserUpdateForm(request.POST,instance=user1)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user1.profile)

            if u_form and p_form.is_valid():
                u_form.save()
                p_form.save()

                messages.success(request, f'Your Account Profile has been updated')
                return redirect('profile')

        else:
            messages.error(request, f"Please, You gotta login first hacker!")
            return redirect('login')

    context={
        'u_form':u_form,
        'p_form': p_form,
        'user': user1,
    }

    return render(request,'users/profile.html',context=context)
