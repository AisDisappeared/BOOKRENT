from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import sweetify
import pyotp

from .forms import * 
from .utils import send_otp
from datetime import datetime



def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                sweetify.success(request, 'signup successful',persistent='ok')
                return redirect('/')
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html',context)
    else:
       return redirect('/')







def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username,password=password)
                if user is not None:
                    send_otp(request)
                    request.session['username'] = username 
                    return redirect('accounts:otp')
                    # login(request,user)
                    # sweetify.success(request,'Login successful' , persistent='ok')
                    # return redirect('/')
                else:
                    sweetify.error(request,'invalid username or password!' , persistent='ok')
                    return redirect('/')
        else:
          form = LoginForm()
          context = {"form":form}
          return render(request,'accounts/login.html',context)
    else:  
        return redirect('/')



def otp_view(request):
    form = OTPForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            otp = form.cleaned_data['otp']
            username = request.session['username']
            otp_secret_key = request.session['otp_secret_key']
            otp_valid_until = request.session['otp_valid_date']

            if otp_secret_key and otp_valid_until:
                valid_until = datetime.fromisoformat(otp_valid_until)
                if valid_until > datetime.now():
                    totp = pyotp.TOTP(otp_secret_key, interval=60)
                    if totp.verify(otp):
                        user = get_object_or_404(User , username=username)
                        login(request,user)
                        del request.session['otp_secret_key']
                        del request.session['otp_valid_date']
                        sweetify.success(request,'Login successful' , persistent='ok')
                        return redirect('/')
                    else:
                        sweetify.error(request, 'invalid one-time password',persistent=':(')
                        return request.META.get('HTTP_REFERER')
                else:
                    sweetify.error(request,'one-time password has expired',persistent=':(')
                    request.META.get('HTTP_REFERER')
            else:
                sweetify.error(request,'Oops! ... something went wrong!',persistent=':(')
                request.META.get('HTTP_REFERER')
    form = OTPForm()
    context = {"form":form}
    return render(request,'accounts/otp.html',context)



@login_required
def logout_view(request):
    logout(request)
    sweetify.success(request,'Logout successful!',persistent='ok')
    return redirect('/')

