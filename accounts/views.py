from django.shortcuts import redirect, render
from .forms import * 
from django.contrib.auth import authenticate , login , logout
import sweetify




def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username,password=password)
                if user is not None:
                    login(request,user)
                    sweetify.success(request,'Login successful' , persistent='ok')
                    return redirect('/')
                else:
                    sweetify.error(request,'invalid username or password!' , persistent='ok')
        else:
          form = LoginForm()
          context = {"form":form}
          return render(request,'accounts/login.html',context)
    else:  
        return redirect('/')
