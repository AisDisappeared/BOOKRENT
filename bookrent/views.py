from django.shortcuts import redirect, render 
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Count,Sum
from bookrent.utils import is_ajax
from rentals.models import Rental
from books.models import *
from customers.models import Customer
from publishers.models import Publisher
from rentals.status import STATUS_CHOICES
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required




def change_mode(request):
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode'] = not request.session['is_dark_mode'] 
    else:
        request.session['is_dark_mode'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'



@login_required
def chart_data(request):
    if not is_ajax(request):
        return redirect('/')

    data = []
    all_books = len(Book.objects.all())
    all_booktitles = len(BookTitle.objects.all())

    data.append({
        'labels':['books','book titles'],
        'data':[all_books,all_booktitles],
        'description':'unique book titles vs books',
        'type':'bar',
    
    })


    titles_by_publisher = BookTitle.objects.values('publisher__name').annotate(Count('publisher__name'))
    publisher_names = [x['publisher__name'] for x in titles_by_publisher]
    publisher_name_count = [x['publisher__name__count'] for x in titles_by_publisher]
    data.append({
        'labels':publisher_names,
        'data':publisher_name_count,
        'description':'book title count by publisher',
        'type':'pie',
    })

    book_by_status = Rental.objects.values('status').annotate(Count('book__book_title'))
    book_title_count = [x['book__book_title__count'] for x in book_by_status]
    status_keys = [x['status'] for x in book_by_status]
    status = [dict(STATUS_CHOICES)[key] for key in status_keys]
    data.append({
        'labels':status,
        'data':book_title_count,
        'description':'book by status',
        'type':'pie',
    })
    
    customers = len(Customer.objects.all())
    publishers = len(Publisher.objects.all())
    data.append({
        'labels':['customers','publishers'],
        'data':[customers,publishers],
        'description':'customers vs publishers',
        'type':'bar',
    })
    return JsonResponse({"data":data})