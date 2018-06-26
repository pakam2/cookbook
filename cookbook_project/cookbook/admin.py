from django.contrib import admin
from cookbook.models import RecipesModel
from django.contrib.auth.models import User
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    
    #Actions
    def spring_season(self, request, queryset):
        #Changing the season of the recipe to spring
        rows_updated = queryset.update(recipe_season = "SP")
        if rows_updated == 1:
            message_bit = "1 season"
        else:
            message_bit = "{} seasons".format(rows_updated)
        self.message_user(request, "{} changed".format(message_bit)) 
    
    def winter_season(self, request, queryset):
        #Changing the season of the recipe to winter
        rows_updated = queryset.update(recipe_season = "WI")
        if rows_updated == 1:
            message_bit = "1 season"
        else:
            message_bit = "{} seasons".format(rows_updated)
        self.message_user(request, "{} changed".format(message_bit)) 


    def summer_season(self, request, queryset):
        #Changing the season of the recipe to summer
        rows_updated = queryset.update(recipe_season = "SU")
        if rows_updated == 1:
            message_bit = "1 season"
        else:
            message_bit = "{} seasons".format(rows_updated)
        self.message_user(request, "{} changed".format(message_bit)) 


    def autumn_season(self, request, queryset):
        #Changing the season of the recipe to autumn
        rows_updated = queryset.update(recipe_season = "WI")
        if rows_updated == 1:
            message_bit = "1 season"
        else:
            message_bit = "{} seasons".format(rows_updated)
        self.message_user(request, "{} changed".format(message_bit)) 



    #Restrict access for non-superusers
    #Restrict access for delete_selected action
    def get_actions(self, request):
        actions = super(RecipeAdmin, self).get_actions(request)
        if request.user.is_superuser == False:
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    #Short description for actions
    winter_season.short_description = "Change the season to winter"
    summer_season.short_description = "Change the season to summer"
    autumn_season.short_description = "Change the season to autumn"
    spring_season.short_description = "Change the season to spring"
    

    def created_date(self):
        #Changing the text for displaying the creation date of a recipe
        return "Recipe created on {}".format(self.recipe_created)
    
    def get_user_name(self):
        #Get username based on the RecipeModel 'recipe_creator' field
        pk = self.recipe_creator
        user = User.objects.get(pk=pk)
        return user.username

    actions = [spring_season, summer_season, autumn_season, winter_season]    
    list_display = ('recipe_title', get_user_name, created_date, 'recipe_season')
    exclude = ['recipe_creator']

class IngredientsAdmin(admin.ModelAdmin):
   
    
    def recipe_title(self, obj):
        #Displays the title of the recipe 
        title = obj.recipe.values_list("recipe_title")
        #Removing "<Queryset...>" string from the reply
        for x in title:
            title = x
        return title



    def ingredients(self, obj):
        full_ingredients_list = [obj.ingredient_one, obj.ingredient_two, obj.ingredient_three,
                                obj.ingredient_four, obj.ingredient_five, obj.ingredient_six,
                                obj.ingredient_seven, obj.ingredient_eight, obj.ingredient_nine,
                                obj.ingredient_ten]
        list_of_ingredients = "" 
        for ingredient in full_ingredients_list:
            if ingredient != "":
                list_of_ingredients += ingredient + ", "

        #Removing the last ',' from string
        length = len(list_of_ingredients)
        list_of_ingredients = list_of_ingredients[0:length - 2]
        return list_of_ingredients
    

    list_display = ('recipe_title', "ingredients")

admin.site.register(RecipesModel, RecipeAdmin)

