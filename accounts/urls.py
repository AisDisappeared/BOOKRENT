from django.urls import path,include 
from .views import * 



urlpatterns = [
    path('login/',login_view,name='login'),
    
]
