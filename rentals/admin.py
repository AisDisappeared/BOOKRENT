from django.contrib import admin
from .models import Rental
from import_export import resources 
from import_export.admin import ExportActionMixin 
from import_export.fields import Field
from . status import STATUS_CHOICES



class RentalResources(resources.ModelResource):
    book = Field()
    book_id = Field()
    status = Field()
    is_closed = Field()
    customer = Field()

    class Meta:
        model = Rental
        fields = ('id','book','book_id','customer','status','is_closed','rent_start_date','rent_end_date','return_date')

    def dehydrate_book(self, obj):
        return obj.book.book_title.title 

    def dehydrate_book_id(self, obj):
        return obj.book.book_id 
    
    def dehydrate_status(self, obj):
        statuses = dict(STATUS_CHOICES)
        return statuses[obj.status]

    def dehydrate_is_closed(self, obj):
        return True if obj.is_closed == 1 else False  
    
    def dehydrate_customer(self, obj):
        return obj.customer.username

class RentalAdmin(ExportActionMixin,admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['book','status','customer','is_closed','created_at','return_date']
    list_filter = ['status']
    search_fields = ['book','status','is_closed'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'
    resource_class = RentalResources




admin.site.register(Rental,RentalAdmin)