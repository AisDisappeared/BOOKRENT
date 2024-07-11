from django import forms

class SearchBookForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"search by book id",'autofocus': 'autofocus'}))
