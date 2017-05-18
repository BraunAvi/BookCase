# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Reader, Book, Review,ReaderE
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from readings.models import ReaderE


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('book', 'reviewed_by', 'rating', 'published_date')
    list_filter = ['published_date', 'reviewed_by']
    search_fields = ['book__name','reviewed_by__username']

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'author', 'year', 'number_of_pages','wiki_page')
    list_filter = ['name', 'author','year']
    search_fields = ['name','author']

class ReadersAdmin(admin.ModelAdmin):
    model = Reader
    list_display = ('username', 'year_of_birth', 'gender')
    list_filter = ['username', 'gender']
    search_fields = ['username']

class ReadersAdminE(admin.ModelAdmin):
    model = ReaderE
    list_display = ['gender',]
    list_filter = ['gender']
    search_fields = ['gender']


class ReaderInline(admin.StackedInline):
    model = ReaderE
    can_delete = False
    verbose_name_plural = 'Reader'
    fk_name = 'user'

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ReaderInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active','is_staff', 'get_gender','get_year')
    list_select_related = ('readere', )

    def get_gender(self, instance):
        return instance.readere.gender
    get_gender.short_description = 'Gender'

    def get_year(self, instance):
        return instance.readere.year_of_birth
    get_year.short_description = 'Y.O.B'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Book,BookAdmin)
admin.site.register(Reader,ReadersAdmin)
admin.site.register(Review, ReviewAdmin)
# admin.site.register(ReaderE,ReadersAdminE)
