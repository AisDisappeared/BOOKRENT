from dataclasses import field
from django.contrib import admin
from .models import * 
from import_export import resources
from import_export.fields import Field 
from import_export.admin import ExportActionMixin 


class BookResource(resources.ModelResource):
    book_title = Field()
    publisher = Field()
    
    class Meta:
        fields  = ['book_title','book_id','Qr_code','publisher']
        model = Book

    # # customizing to show some model fields in exporting functionality 
    def dehydrate_book_title(self, obj):
        return obj.book_title.title

    # def dehydrate_status(self, obj):
    #     return obj.status

    def dehydrate_publisher(self, obj):
        return obj.book_title.publisher.name




class BookTitleAdmin(admin.ModelAdmin):
    list_display = ['title','author','publisher'] 
    list_filter = ['author','publisher']
    date_hierarchy = 'created_at'
    search_fields = ['title','author'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'





class BookAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ['book_title']
    list_filter = ['book_title']
    date_hierarchy = 'created_at'
    search_fields = ['book_title'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'
    resource_class = BookResource



admin.site.register(BookTitle,BookTitleAdmin)
admin.site.register(Book,BookAdmin)


