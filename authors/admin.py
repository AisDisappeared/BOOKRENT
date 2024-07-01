from django.contrib import admin
from .models import Author 


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'

    
admin.site.register(Author,AuthorAdmin)
