# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0003_auto_20170513_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Review',
            new_name='body',
        ),
    ]
