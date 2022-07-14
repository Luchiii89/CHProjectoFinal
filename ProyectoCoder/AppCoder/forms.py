from django import forms


class BookForm(forms.Form):
    title = forms.CharField()
    genre = forms.IntegerField()
    year = forms.IntegerField()

class AuthorForm(forms.Form):   
    name = forms.CharField(max_length=40)
    surname = forms.CharField(max_length=40)
    country= forms.CharField(max_length=25)
    email = forms.EmailField()