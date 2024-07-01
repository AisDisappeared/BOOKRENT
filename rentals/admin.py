from django.contrib import admin
from .models import Rental


class RentalAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['book','status','customer','is_closed','created_at','return_date']
    list_filter = ['status']
    search_fields = ['book','status','is_closed'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'


admin.site.register(Rental,RentalAdmin)