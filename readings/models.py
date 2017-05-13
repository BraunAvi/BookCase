# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
import numpy as np

class Reader(models.Model):
    GENDER_CHOICES=(
        ('M','male'),
        ('F','female'),
        ('O','not/specified')
    )

    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
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
    illustrator = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    # year_1st_published = models.CharField(max_length=50)
    year = models.IntegerField(default=datetime.datetime.now().year)

    number_of_pages = models.IntegerField()

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    book = models.ForeignKey(Book)
    reviewed_by = models.ForeignKey(Reader)
    pub_date = models.DateTimeField('date published')
    Review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __unicode__(self):
        return self.book.name + ' by '+self.reviewed_by.username

