from django.urls import path,include
from .views import * 

app_name = 'books'

urlpatterns = [
    path('',BookTitleListView.as_view(),name='books'),    
]
