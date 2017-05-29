# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import URLValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

import datetime
import numpy as np

class Reader(models.Model):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'Other /not specified')
    )

    YEAR_CHOICES = []
    YEAR_CHOICES.append((1000,'1000'))

    for r in range(1890, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))
    # user_id=models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='O')
    year_of_birth = models.IntegerField(choices=YEAR_CHOICES, default=1000)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Reader.objects.create(user=instance)
        instance.reader.save()

# class Reader(models.Model):
#     GENDER_CHOICES=(
#         ('M','male'),
#         ('F','female'),
#         ('O','not/specified')
#     )
#
#     YEAR_CHOICES = []
#     for r in range(1910, (datetime.datetime.now().year + 1)):
#         YEAR_CHOICES.append((r, r))
#
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     year_of_birth = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year-10)
#     gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
#     password = models.CharField(max_length=50)
#     join_date = models.DateTimeField('date joined')
#
#     def __unicode__(self):
#         return self.username

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    illustrator = models.CharField(max_length=50,blank=True)
    publisher = models.CharField(max_length=50,blank=True)
    year = models.IntegerField(default=datetime.datetime.now().year,blank=True)
    wiki_page = models.CharField(max_length=200, blank=True,  validators=[URLValidator()])
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
    reviewed_by = models.ForeignKey(User)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    body = models.TextField()
    quote = models.CharField(max_length=200,blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __unicode__(self):
        return self.book.name + ' by '+self.reviewed_by.username

    objects = models.Manager() # the default manager (used for queries for example)
