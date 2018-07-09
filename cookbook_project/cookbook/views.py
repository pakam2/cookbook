from django.shortcuts import render, redirect
from django.views import View
from cookbook.forms import RecipeForm, SignUpForm, LoginForm, ShowRecipesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from cookbook.models import RecipesModel


# Create your views here.

class MainView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'main.html')

    def post(self, request):
        return render(request, 'main.html')

class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            login_name = form.cleaned_data['login']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            #TODO create a validator for password check
            if password1 == password2:
                user = User.objects.create_user(first_name = first_name, last_name=last_name, username=login_name, password=password1)
                user.save()
                return HttpResponse("New user added")
            else:
                return HttpResponse("Something went wrong")
        return HttpResponse('Data not valid')
class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        username = request.POST['login_field']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            return HttpResponse("There is no such user")

class LogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')


class AddRecipeView(LoginRequiredMixin, View):

    def get(self, request):
        form_recipe = RecipeForm()
        return render(request, 'add_recipe.html', {'form': form_recipe})

    
    def post(self, request):
        new_form = RecipeForm()

        form = RecipeForm(request.POST)
        if form.is_valid():
            pass
        recipe_title = form['recipe_title'].value()
        recipe_season = form['recipe_season'].value()
        ingredient_one = form['ingredient_one'].value()
        ingredient_two = form['ingredient_two'].value()
        ingredient_three = form['ingredient_three'].value()
        ingredient_four = form['ingredient_four'].value()
        ingredient_five = form['ingredient_five'].value()
        ingredient_six = form['ingredient_six'].value()
        ingredient_seven = form['ingredient_seven'].value()
        ingredient_eight = form['ingredient_eight'].value()
        ingredient_nine = form['ingredient_nine'].value()
        ingredient_ten = form['ingredient_ten'].value()            

        logged_user = User.objects.get(username=request.user)
        print(logged_user.id)
        new_recipe = RecipesModel.objects.create(recipe_title=recipe_title, recipe_season=recipe_season, recipe_creator=logged_user.id, ingredient_one=ingredient_one,
                                   ingredient_two=ingredient_two, ingredient_three=ingredient_three, ingredient_four=ingredient_four, ingredient_five=ingredient_five,
                                   ingredient_six=ingredient_six, ingredient_seven=ingredient_seven, ingredient_eight=ingredient_eight, ingredient_nine=ingredient_nine,
                                   ingredient_ten=ingredient_ten)
        new_recipe.save()

        return render(request, 'add_recipe.html', {'form': new_form, 'ctx': "Added a new recipe: '{}'".format(recipe_title)})



class ShowRecipesView(LoginRequiredMixin, View):

    def get(self, request):
        form = ShowRecipesForm()
        return render(request, 'get_recipes.html', {'form': form})


    def post(self, request):
        form = request.POST
        recipes = RecipesModel.objects.filter(recipe_creator=request.user.id, recipe_season=form['recipe_season'])
        return render(request, 'show_recipes.html', {'recipes': recipes}) 

class RecipeDetailView(LoginRequiredMixin, View):

    def get(self, request, id):
        recipe = RecipesModel.objects.filter(recipe_creator=request.user.id, id =id)
        return render(request, 'recipe_detail.html', {'recipe': recipe})
