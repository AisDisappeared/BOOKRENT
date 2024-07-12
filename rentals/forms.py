from django import forms
from .status import FORMAT_CHOICES


class SearchBookForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"search by book id",'autofocus': 'autofocus'}))


class SelectExportOptionForm(forms.Form):
    format = forms.ChoiceField(choices=FORMAT_CHOICES,widget=forms.RadioSelect())