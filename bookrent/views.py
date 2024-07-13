from django.shortcuts import render 
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Count,Sum

from books.models import *

def change_mode(request):
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode'] = not request.session['is_dark_mode'] 
    else:
        request.session['is_dark_mode'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




class DashboardView(TemplateView):
    template_name = 'dashboard.html'





def chart_data(request):
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
    print(data)
    return JsonResponse({"msg":"hello to chart data view"})