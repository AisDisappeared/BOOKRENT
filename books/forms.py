from django import forms 
from .models import * 
from django.core.exceptions import ValidationError

class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('title','publisher','author')

    def clean(self):
        title = self.cleaned_data['title']
        
        if len(title) < 5:
            error_msg = 'Your Book title should be 5 characters at least!'
            raise ValidationError(error_msg)
    
        book_title_exist = BookTitle.objects.filter(title__iexact=title).exists()
        if book_title_exist:
            duplicate_error_msg = 'Book with this title already exists'
            raise ValidationError(duplicate_error_msg)
        
        return self.cleaned_data
