# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_one', models.CharField(max_length=200)),
                ('ingredient_two', models.CharField(max_length=200)),
                ('ingredient_three', models.CharField(max_length=200)),
                ('ingredient_four', models.CharField(max_length=200)),
                ('ingredient_five', models.CharField(max_length=200)),
                ('ingredient_six', models.CharField(max_length=200)),
                ('ingredient_seven', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RecipesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_title', models.CharField(max_length=200)),
                ('recipe_created', models.DateField(auto_now_add=True)),
                ('recipe_season', models.CharField(choices=[('SP', 'Spring'), ('SU', 'Summer'), ('AU', 'Autumn'), ('WI', 'Winter')], max_length=2)),
            ],
        ),
    ]
