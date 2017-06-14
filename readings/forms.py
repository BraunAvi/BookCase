from django import forms
from .models import Review, Book
from .models import Document


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ('book','body','quote','rating','reviewed_by')
        fields = ('book','body','quote','rating') # reviewed by is added automatically



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','author','illustrator','publisher','year','number_of_pages','wiki_page','cover_image')



# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('description', 'cover_image', )