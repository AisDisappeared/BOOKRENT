from django.contrib import admin
from .models import Publisher 


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name','country']
    list_filter = ['name','country']
    date_hierarchy = ('created_at')
    search_fields = ['name','country'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'

admin.site.register(Publisher,PublisherAdmin)