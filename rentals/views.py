from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from books.forms import BookTitleForm
from .models import Rental 
from .forms import SearchBookForm 
from books.models import Book
import sweetify




def AllRentals(request):
    form = SearchBookForm()
    rentobjects = Rental.objects.all()
    context = {"form":form,"rentobjects":rentobjects}
    return render(request,'rentals/main.html',context)


def RentalSearchView(request):
    if request.method == 'GET':
        form = SearchBookForm(request.GET)
        if form.is_valid():
            s = request.GET.get('text')
            book = Book.objects.filter(book_id=s)
            if not book:
                sweetify.error(request,'book doesn\' exist',persistent='ok')
            context = {"book":book}
            return render(request,'rentals/search.html',context)
