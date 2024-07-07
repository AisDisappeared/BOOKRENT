from django.urls import path,include
from .views import * 

app_name = 'books'

urlpatterns = [
    path('',BookTitleListView.as_view(), {'char' : None} , name='books'),
    path('<str:char>/',BookTitleListView.as_view(),name='char-books'),
]
