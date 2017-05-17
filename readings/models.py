# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
import numpy as np
from django.core.validators import URLValidator

from django.utils import timezone


class Reader(models.Model):
    GENDER_CHOICES=(
        ('M','male'),
        ('F','female'),
        ('O','not/specified')
    )

    YEAR_CHOICES = []
    for r in range(1890, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    year_of_birth = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year-10)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    password = models.CharField(max_length=50)
    join_date = models.DateTimeField('date joined')

    def __unicode__(self):
        return self.username

class Book(models.Model):
    # YEAR_CHOICES = []
    # for r in range(1700, (datetime.datetime.now().year + 1)):
    #     YEAR_CHOICES.append((r, r))

    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    illustrator = models.CharField(max_length=50,blank=True)
    publisher = models.CharField(max_length=50,blank=True)
    year = models.IntegerField(default=datetime.datetime.now().year,blank=True)
    wiki_page = models.CharField(max_length=100, blank=True,  validators=[URLValidator()])
    number_of_pages = models.IntegerField(blank=True)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, 'did\'nt like it so much'),
        (2, 'thought it was OK'),
        (3, 'Loved it!'),
    )
    # id = models.IntegerField(unique=True, db_index=True, blank=True, primary_key=True, null=False,auto_created=True)

    book = models.ForeignKey(Book)
    reviewed_by = models.ForeignKey(Reader)
    published_date = models.DateTimeField('date published')
    body = models.TextField()
    quote = models.CharField(max_length=500, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    # rating_text = models.CharField(max_length=30,default=rating)


    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __unicode__(self):
        return self.book.name + ' by '+self.reviewed_by.username

    objects = models.Manager() # the default manager (used for queries for example)
