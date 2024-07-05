from django.shortcuts import render
from .models import *


def BookList(request):
    books = BookTitle.objects.all().order_by('title')
    context = {"books":books}
    return render(request,'books/books-list.html',context)


