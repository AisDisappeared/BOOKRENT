from django.contrib import admin
from .models import Publisher 


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name','country']
    list_filter = ['name','country']
    date_hierarchy = ('created_at')

admin.site.register(Publisher,PublisherAdmin)