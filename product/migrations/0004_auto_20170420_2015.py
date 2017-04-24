# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 12:15
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('product', '0003_auto_20170420_1607'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Username',
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
