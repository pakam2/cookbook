# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-28 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0006_recipesmodel_recipe_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientsmodel',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_eight',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_five',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_four',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_nine',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_one',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_seven',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_six',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_ten',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_three',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='recipesmodel',
            name='ingredient_two',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='IngredientsModel',
        ),
    ]
