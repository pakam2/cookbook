from django import forms
from django.forms import ModelForm
from cookbook.models import RecipesModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RecipeForm(ModelForm):
    
    class Meta:
        model = RecipesModel
        fields = '__all__'

class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=200, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=200, required=False, help_text="Optional")
    email = forms.EmailField(max_length=400)
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text="") 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    
    email_field = forms.EmailField(max_length=400)
    password = forms.CharField(widget=forms.PasswordInput())



