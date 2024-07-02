from django.contrib import admin
from .models import Customer 
from import_export.admin import ExportActionMixin 
from import_export import resources 
from import_export.fields import Field

class CustomerResource(resources.ModelResource):
    additional_info = Field()
    books = Field()
    class Meta:
        fields = ['id','first_name','last_name','username','rating','books', 'books_count', 'additional_info']
        model = Customer
        export_order = fields 

    def dehydrate_additional_info(self , obj):
        if len(obj.additional_info) == 0:
            return '-'
        elif len(obj.additional_info) == 5:
            return obj.additional_info 
        else:
            Ai_list = obj.additional_info.split(" ")[:5]
            Ai_list = "".join(Ai_list)
            return Ai_list + "..."


    def dehydrate_books(self, obj):
        Books = [x.book_id for x in obj.books.all()]
        return ", ".join(Books)



# Custom Admin Class should first inherit from ExportActionMixin and then ModelAdmin class 
class CustomerAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ['username','rating','books_count']
    list_filter = ['username','rating']
    ordering = ['-rating']
    search_fields = ['username'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'
    resource_class = CustomerResource



admin.site.register(Customer,CustomerAdmin)