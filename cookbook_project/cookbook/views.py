from django.shortcuts import render, redirect
from django.views import View
from cookbook.forms import RecipeForm, SignUpForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User



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
