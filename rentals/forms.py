from django import forms

class SearchBookForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={"placeholer":"search by book id"}))
