# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 12:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaflet_news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='New',
            new_name='NewsPost',
        ),
    ]
