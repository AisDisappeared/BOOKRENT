from django.contrib import admin
from .models import Publisher 
from import_export import resources 
from import_export.admin import ExportActionMixin 
from import_export.fields import Field


class PublisherResource(resources.ModelResource):
    created_at = Field()
    class Meta:
        fields = ['id','name','country','created_at']
        model = Publisher
        export_order = fields 


    def dehydrate_created_at(self , obj):
        return obj.created_at.strftime('%d/%m/%y')
    

class PublisherAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ['name','country']
    list_filter = ['name','country']
    date_hierarchy = ('created_at')
    search_fields = ['name','country'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'
    resource_class = PublisherResource


admin.site.register(Publisher,PublisherAdmin)