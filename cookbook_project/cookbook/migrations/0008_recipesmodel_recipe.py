# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0007_auto_20180628_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipesmodel',
            name='recipe',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
