from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import *
from django.views import generic
from .forms import * 
from django.contrib import messages
import string




class BookTitleListView(generic.FormView,generic.ListView):
    model = BookTitle
    template_name = 'books/books-list.html'
    context_object_name = 'books'
    form_class = BookTitleForm
    success_url = reverse_lazy('books:books')
    i_instance = None


    # override get queryset method to avoid from recieving no object_list error.
    def get_queryset(self):
        selected_char = self.kwargs.get('char') if self.kwargs.get('char') else 'A'
        return BookTitle.objects.filter(title__startswith=selected_char)        


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        letters = list(string.ascii_uppercase)
        context['letters'] = letters
        selected_letter = self.kwargs.get('char')
        context['selected_letter'] = selected_letter if self.kwargs.get('char') else 'A'
        return context

    # form valid method 
    def form_valid(self, form: BookTitleForm) -> HttpResponse:
        self.i_instance = form.save()
        messages.add_message(self.request,messages.INFO,f"book title:{self.i_instance.title} has been created")
        return super().form_valid(form)
    
    # form invalid method 
    def form_invalid(self, form: BookTitleForm):
        self.object_list = self.get_queryset()
        messages.add_message(self.request,messages.ERROR,form.errors)
        return super().form_invalid(form)
        
    

    

class BookTitleDetailView(generic.DetailView):
    model = BookTitle
    template_name = 'books/book-detail.html'





class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/singlebook.html'

    def get_object(self):
        Allbooks = Book.objects.all()
        id = self.kwargs.get('book_id')
        book_requested = get_object_or_404(Allbooks,id=id)
        return book_requested
    



class BookDeleteView(generic.DeleteView):
    model = Book 
    template_name = 'books/confirm_delete.html'

    def get_object(self):
        Allbooks = Book.objects.all()
        id = self.kwargs.get('book_id')
        book_requested = get_object_or_404(Allbooks,id=id)
        return book_requested
    

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, f"book with {self.get_object().book_id} has been deleted")
        letter = self.kwargs.get('char')
        slug = self.kwargs.get('slug')
        return reverse('books:book-detail',kwargs={"char":letter,"slug":slug})