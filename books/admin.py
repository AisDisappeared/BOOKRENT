from django.contrib import admin
from .models import * 



class BookTitleAdmin(admin.ModelAdmin):
    list_display = ['title','author','publisher'] 
    list_filter = ['author','publisher']
    date_hierarchy = 'created_at'



class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title']
    list_filter = ['book_title']
    date_hierarchy = 'created_at'


admin.site.register(BookTitle,BookTitleAdmin)
admin.site.register(Book,BookAdmin)


