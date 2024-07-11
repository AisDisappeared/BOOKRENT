from django.db import models
from books.models import Book 
from customers.models import Customer
from datetime import timedelta 
from django.urls import reverse
from .status import STATUS_CHOICES


class Rental(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE) 
    status = models.CharField(max_length=2 , choices=STATUS_CHOICES)
    rent_start_date = models.DateField(help_text='when the book was rented')
    rent_end_date = models.DateField(blank=True,help_text='deadline')
    return_date = models.DateField(blank=True,help_text='actual return date',null=True)
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']


    def status_text(self):
        statuses = dict(STATUS_CHOICES)
        return statuses[self.status]

    # get absolute url method 
    def get_absolute_url(self):
        return reverse("rentals:detail",kwargs={"book_id":self.book.book_id})
    

    
    def save(self, *args, **kwargs):
        if not self.rent_end_date:
            self.rent_end_date = self.rent_start_date + timedelta(days=14)
        super().save(*args, **kwargs)



    def __str__(self):
        return f"{self.book.book_id} rented by {self.customer.username}"