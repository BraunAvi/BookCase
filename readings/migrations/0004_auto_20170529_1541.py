# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0003_auto_20170521_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
