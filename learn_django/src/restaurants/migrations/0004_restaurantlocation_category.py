# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-08-20 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20190820_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(max_length=120, null=True),
        ),
    ]