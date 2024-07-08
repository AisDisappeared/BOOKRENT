from django.urls import path,include
from .views import * 

app_name = 'books'

urlpatterns = [
    path('',BookTitleListView.as_view(), {'char' : None} , name='books'),
    path('<str:char>/',BookTitleListView.as_view(),name='char-books'),
    path('<str:char>/<slug>/',BookTitleDetailView.as_view(),name='book-detail'),
    path('<str:char>/<slug>/<str:book_id>/',BookDetailView.as_view(),name='detail'),
    path('<str:char>/<slug>/<str:book_id>/delete',BookDeleteView.as_view(),name='book-delete'),
]
