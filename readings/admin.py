# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin

from .models import Reader, Book, Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('book', 'reviewed_by', 'rating', 'published_date')
    list_filter = ['published_date', 'reviewed_by']
    search_fields = ['book__name','reviewed_by__username']

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'author', 'year', 'number_of_pages')
    list_filter = ['name', 'author','year']
    search_fields = ['name','author']

class ReadersAdmin(admin.ModelAdmin):
    model = Reader
    list_display = ('username', 'year_of_birth', 'gender')
    list_filter = ['username', 'gender']
    search_fields = ['username']

admin.site.register(Book,BookAdmin)
admin.site.register(Reader,ReadersAdmin)
admin.site.register(Review, ReviewAdmin)