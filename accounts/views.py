from django.shortcuts import render
from .forms import * 
from django.contrib.auth import authenticate , login , logout
import sweetify




def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data('username')
                password = form.cleaned_data('password')
                user = authenticate(request, username=username,password=password)
                if user is not None:
                    pass 
                else:
                    sweetify.error(request,'invalid username or password!' , persistent='ok')




    context = {"forn":form}
    return render(request,'accounts/login.html',context)