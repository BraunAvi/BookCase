# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0031_auto_20170519_0014'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReaderE',
            new_name='Reader',
        ),
    ]
