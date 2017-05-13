from django import forms
from models import *

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Reader
        fields = ('name', 'email', 'password',)
