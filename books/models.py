from pyexpat import model
from django.db import models
from publishers.models import Publisher 
from authors.models import Author
from django.utils.text import slugify

class BookTitle(models.Model):
    title = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(blank=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    author  = models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # save method for generating slug field .... even an object from booktitle model doesn't have slug .
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a slug 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title}"
    



class Book(models.Model):
    book_title = models.ForeignKey(BookTitle,on_delete=models.CASCADE)
    book_id = models.CharField(max_length=255,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)
    # Qr_code 

    def __str__(self):
        return f"{self.book_title}"