# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0010_auto_20170516_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating_text',
            field=models.CharField(default=models.IntegerField(choices=[(1, "did'nt like it so much"), (2, 'thought it was OK'), (3, 'Loved it!')]), max_length=30),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, "did'nt like it so much"), (2, 'thought it was OK'), (3, 'Loved it!')]),
        ),
    ]