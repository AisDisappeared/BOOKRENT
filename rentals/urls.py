from django.urls import path,include

from .views import *


app_name = 'rentals'
urlpatterns = [
    path('',AllRentals,name='rentals'),
    path('search/',RentalSearchView,name='rental-search'),

]
