from django.db import models
from books.models import Book
from django.utils.text import slugify


class Customer(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    username = models.CharField(max_length=255,unique=True,blank=True)
    additional_info = models.TextField(blank=True,null=True)
    rating = models.PositiveSmallIntegerField(default=20)
    books = models.ManyToManyField(Book,blank=True,help_text='books that are currently rented')
    books_count = models.PositiveSmallIntegerField(default=0)

    # override django save method
    def save(self , *args, **kwargs):
        if not self.username:
            username = slugify(f"{self.first_name} {self.last_name}")
            ex = __class__.objects.fitler(username=username).exit()
            
            while ex:
                i = len(__class__.objects.filter(first_name=self.first_name,last_name=self.last_name))
                username = slugify(f"{self.first_name} {self.last_name} {i+1}")
                ex = __class__.objects.fitler(username=username).exit()

            self.username = username

        super().save(*args, **kwargs)
 

    def __str__(self):
        return f"{self.username}"
    
