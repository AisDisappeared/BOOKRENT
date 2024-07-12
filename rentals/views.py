from audioop import reverse
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.views.generic import ListView,UpdateView
from django.shortcuts import redirect, render
from books.forms import BookTitleForm
from .models import *
from .forms import SearchBookForm 
from books.models import Book
import sweetify


class BookRentalHistoryView(ListView):
    model = Rental
    template_name = 'rentals/detail.html'

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Rental.objects.filter(book__book_id=book_id)


def RentalSearchView(request):
    rentobjects = Rental.objects.all()
    
    if request.method == 'GET':
        form = SearchBookForm(request.GET)
        if form.is_valid():
            s = request.GET.get('text')
            book = Book.objects.filter(book_id=s).exists()
            if s is not None and book: 
                return redirect('rentals:detail',s)
            elif s is not None and not book:
                return render(request,'rentals/404.html')
            
        context = {"form":form,"rentobjects":rentobjects}
        return render(request,'rentals/main.html',context)
    


# we don't have to create a form seperately when we are using from updateview ... it creates it for us .
class RentalStatusUpdateView(UpdateView):
    model = Rental
    template_name = 'rentals/update.html'
    fields = ('status',)