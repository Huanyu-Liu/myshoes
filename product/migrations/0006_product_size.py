# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.IntegerField(default=40),
        ),
    ]
