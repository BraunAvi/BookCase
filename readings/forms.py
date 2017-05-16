from django import forms
from .models import Review, Reader, Book


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('book','body','quote','rating','reviewed_by')



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','author','illustrator','publisher','year','number_of_pages')

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Reader
        fields = ('username', 'email', 'password',)
