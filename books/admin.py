from django.contrib import admin
from .models import * 



class BookTitleAdmin(admin.ModelAdmin):
    list_display = ['title','author','publisher'] 
    list_filter = ['author','publisher']
    date_hierarchy = 'created_at'
    search_fields = ['title','author'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'



class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title']
    list_filter = ['book_title']
    date_hierarchy = 'created_at'
    search_fields = ['book_title'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'


admin.site.register(BookTitle,BookTitleAdmin)
admin.site.register(Book,BookAdmin)


