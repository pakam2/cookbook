from django.contrib import admin
from cookbook.models import RecipesModel, IngredientsModel
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_title', 'recipe_created', 'recipe_season')

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient_one', 'ingredient_two', 'ingredient_three', 'ingredient_four',
                    'ingredient_five', 'ingredient_six', 'ingredient_seven', 'ingredient_eight',
                   'ingredient_nine', 'ingredient_ten')
    empty_value_display = "empty"

admin.site.register(RecipesModel, RecipeAdmin)
admin.site.register(IngredientsModel, IngredientsAdmin)

