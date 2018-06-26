from django.db import models

# Create your models here.


SEASONS = (  ("SP", "Spring"),
            ("SU", "Summer"),
            ("AU", "Autumn"),
            ("WI","Winter"),
            )

class RecipesModel(models.Model):

    recipe_title = models.CharField(max_length=200)
    recipe_created = models.DateField(auto_now_add = True)
    recipe_season = models.CharField(max_length=2, choices=SEASONS)

    def __str__(self):
        return "Recipe title: {}, recipe created on: {}".format(self.recipe_title, self.recipe_created)


class IngredientsModel(models.Model):

    ingredient_one = models.CharField(max_length=200, blank=True)
    ingredient_two = models.CharField(max_length=200, blank=True)
    ingredient_three = models.CharField(max_length=200, blank=True)
    ingredient_four = models.CharField(max_length=200, blank=True)
    ingredient_five = models.CharField(max_length=200, blank=True)
    ingredient_six = models.CharField(max_length=200, blank=True)
    ingredient_seven = models.CharField(max_length=200, blank=True)
    ingredient_eight = models.CharField(max_length=200, blank=True)
    ingredient_nine = models.CharField(max_length=200, blank=True)
    ingredient_ten = models.CharField(max_length=200, blank=True)
    recipe = models.ManyToManyField(RecipesModel)


    def __str__(self):
        list_of_ingredients = [self.ingredient_one, self.ingredient_two, self.ingredient_three, self.ingredient_four, self.ingredient_five]
        print("List of all ingredients:")
        for ingredient in list_of_ingredients:
            if not ingredient == "":
                print("- name of ingredient: {}".format(ingredient))
        return ""
