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

class IngredientsModel(models.Model):
    
    pass



