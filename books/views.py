from django.shortcuts import render
from .models import *
from django.views import generic 

class BookTitleListView(generic.ListView):
    model = BookTitle
    template_name = 'books/books-list.html'
    context_object_name = 'books'