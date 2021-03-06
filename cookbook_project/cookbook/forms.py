from django import forms
from django.forms import ModelForm
from cookbook.models import RecipesModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

SEASONS = (  ("SP", "Spring"),
            ("SU", "Summer"),
            ("AU", "Autumn"),
            ("WI","Winter"),
            )

def checkLogin(val):
    if val == "aa":
        raise ValidationError("Cannot have this value")

class RecipeForm(ModelForm):

    class Meta:
        model = RecipesModel
        fields = '__all__'

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=200, required=False, help_text="Optional")
    login = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=200, required=False, help_text="Optional")
    email = forms.EmailField(max_length=400)
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text="")
    class Meta:
        model = User
        fields = ['login', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(forms.Form):

    login_field = forms.CharField(max_length=400, validators=[checkLogin])
    password = forms.CharField(widget=forms.PasswordInput())


class ShowRecipesForm(ModelForm):

    class Meta:
        model = RecipesModel
        fields = ['recipe_season']
