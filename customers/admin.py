from django.contrib import admin
from .models import Customer 


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username','rating','books_count']
    list_filter = ['username','rating']
    ordering = ['-rating']
    search_fields = ['username'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'
 
admin.site.register(Customer,CustomerAdmin)