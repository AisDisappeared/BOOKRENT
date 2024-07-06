from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.views import generic
from .forms import * 


class BookTitleListView(generic.FormView,generic.ListView):
    model = BookTitle
    template_name = 'books/books-list.html'
    context_object_name = 'books'
    form_class = BookTitleForm
    success_url = reverse_lazy('books:books')

    # override get queryset method to avoid from recieving no object_list error.
    def get_queryset(self):
        return BookTitle.objects.all()

    # form valid method 
    def form_valid(self, form: BookTitleForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)
    
    # form invalid method 
    def form_invalid(self, form: BookTitleForm):
        self.object_list = self.get_queryset()
        return super().form_invalid(form)
        
    