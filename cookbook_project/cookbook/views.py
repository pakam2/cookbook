from django.shortcuts import render
from django.views import View
from cookbook.forms import RecipeForm, SignUpForm, LoginForm


# Create your views here.

class MainView(View):

    def get(self, request):
        form = RecipeForm()
        return render(request, 'main.html', {'form': form})

class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

class LoginView(View):
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
