from audioop import reverse
from http.cookiejar import LWPCookieJar
from typing import Any
from urllib import request, response
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *
from django.db.models import Q
from django.shortcuts import redirect, render
from books.forms import BookTitleForm
from .models import *
from .forms import *
from datetime import datetime
from books.models import Book
from .status import FORMAT_CHOICES
from .admin import RentalResources
import sweetify






class BookRentalHistoryView(ListView):
    model = Rental
    template_name = 'rentals/detail.html'

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Rental.objects.filter(Q(book__book_id=book_id) | Q(book_id=book_id))


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('book_id')
        obj = Book.objects.filter(Q(id=id) | Q(book_id=id))
        context['object'] = obj 
        context['id'] = id 
        return context




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


    def get_success_url(self):
        book_id = self.kwargs.get('book_id')
        return reverse('rentals:detail',kwargs={"book_id":book_id})
    
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        if instance.status == '#1':
            instance.return_date = datetime.today().date()
            instance.is_closed = True 
        instance.save()
        sweetify.success(self.request, 'Rental status updated successfully!',persistent='thanks')
        return super().form_valid(form)
    
    



class NewRentView(CreateView):
    model = Rental
    template_name = 'rentals/newrent.html'
    fields = ('customer',)

    def get_success_url(self):
        book_id = self.kwargs.get('book_id')
        return reverse('rentals:detail',kwargs={"book_id":book_id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.kwargs.get('book_id')
        return context


    def form_valid(self, form):
        instance = form.save(commit=False)
        id = self.kwargs.get('book_id')
        obj = Book.objects.get(id=id)
        instance.book = obj
        instance.status = '#0'
        instance.rent_start_date = datetime.today().date()
        instance.save()
        return super().form_valid(form)
    



class DownloadRentalsView(FormView):
    template_name = 'rentals/select_format.html'
    form_class = SelectExportOptionForm


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('book_id')
        context['id'] = id 
        return context

    def get_success_url(self):
        return self.request.path
    
    def post(self,request,**kwargs):
        formats = dict(FORMAT_CHOICES)
        format = self.request.POST.get('format')
        format = formats[format]

        book_id = self.kwargs.get('book_id')
        qs = Rental.objects.filter(Q(book__book_id=book_id) | Q(book_id=book_id))
        dataset = RentalResources().export(qs)

        if format == 'csv':
            ds = dataset.csv 
        elif format == 'yaml':
            ds = dataset.yaml 
        else:
            ds = dataset.json 
        response = HttpResponse(ds, content_type=format)
        response['Content-Disposition'] = f'attachment; filename=rentals.{format}'
        return response