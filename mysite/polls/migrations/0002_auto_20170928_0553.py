# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 05:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qusetion',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
