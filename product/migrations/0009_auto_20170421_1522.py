# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 07:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20170421_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='count',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
