from django import forms 
from .models import * 


class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('title','publisher','author')

    def clean(self):
        title = self.cleaned_data['title']
        
        if len(title) < 5:
            error_msg = 'Your Book title should be 5 characters at least!'
            raise forms.ValidationError(error_msg)
        return self.cleaned_data