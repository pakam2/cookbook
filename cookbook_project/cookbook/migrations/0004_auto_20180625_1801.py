# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0003_auto_20180615_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientsmodel',
            old_name='ingredinet_eight',
            new_name='ingredient_eight',
        ),
        migrations.AlterField(
            model_name='ingredientsmodel',
            name='ingredient_one',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
