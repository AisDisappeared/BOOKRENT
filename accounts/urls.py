from django.urls import path,include 
from .views import * 



app_name = 'accounts'

urlpatterns = [
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'), 
    path('otp/',otp_view,name='otp'),
]
