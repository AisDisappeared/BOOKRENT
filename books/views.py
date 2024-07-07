from django.http import HttpResponse
from django.shortcuts import render
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
        
    
