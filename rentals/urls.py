from django.urls import path,include

from .views import *


app_name = 'rentals'
urlpatterns = [
    path('',RentalSearchView,name='rental-search'),
    path('book-history/<str:book_id>/',BookRentalHistoryView.as_view(),name='detail'),
    path('book-history/<str:book_id>/<pk>/update-status',RentalStatusUpdateView.as_view(),name='update'),
    path('<str:book_id>/new',NewRentView.as_view(),name='newrent'),
]
