from pyexpat import model
from django.db import models
from publishers.models import Publisher 
from authors.models import Author
from django.utils.text import slugify
import uuid 
from django.urls import reverse

# Packages that we have to import to generate Qrcode
import qrcode 
from io import BytesIO 
from PIL import Image
from django.core.files import File 

from rentals.status import STATUS_CHOICES


class BookTitle(models.Model):
    title = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(blank=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    author  = models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # new field ===> book object . model below
    @property
    def get_books(self):
        return self.book_set.all()
        

    # save method for generating slug field .... even an object from booktitle model doesn't have slug .
    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a slug 
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


    # get absolute url method 
    def get_absolute_url(self):
        char = self.title[:1]
        return reverse("books:book-detail",kwargs={"slug":self.slug,"char":char})
    
    # magic str method 
    def __str__(self):
        return f"{self.title}"
    










class Book(models.Model):
    book_title = models.ForeignKey(BookTitle,on_delete=models.CASCADE)
    book_id = models.CharField(max_length=255,blank=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)
    Qr_code = models.ImageField(upload_to='Qr_codes/',blank=True,null=True)


    # get absolute url method 
    def get_absolute_url(self):
        char = self.book_title.title[:1]
        return reverse("books:detail",kwargs={"slug":self.book_title.slug,"char":char , "book_id":self.book_id})
    

    # defining a new field by using decorator functions --- property
    @property 
    def get_status(self):
        if len(self.rental_set.all()) > 0:
            statuses = dict(STATUS_CHOICES)
            return statuses[self.rental_set.first().status]
        return False


    @property
    def is_available(self):
        if len(self.rental_set.all()) > 0:
            status = self.rental_set.first().status
            return True if status == '#1' else False
        return True


    # book delete absolute url
    def delete_object(self):
        char = self.book_title.title[:1]
        return reverse('books:book-delete',kwargs={'slug':self.book_title.slug,"char":char,"book_id":self.book_id})        


    # overriding django save method 
    def save(self, *args, **kwargs):
        if not self.book_id:
            self.book_id = str(uuid.uuid4()).replace('-','')[:24].lower()

        # Generate one
        qrcode_image = qrcode.make(self.book_id)
        canvas = Image.new('RGB',(qrcode_image.pixel_size,qrcode_image.pixel_size),'white')
        canvas.paste(qrcode_image)
        fname = f"qr_code={self.book_title}.png"
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.Qr_code.save(fname, File(buffer),save=False)
        canvas.close() 
        super().save(*args, **kwargs)


    # magic str method 
    def __str__(self):
        return f"{self.book_title}"