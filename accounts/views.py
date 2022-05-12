from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import csv
from django.contrib.auth.decorators import login_required
from Home.models import Recipe
from django.contrib.auth.models import User
# Create your views here.
from .models import *
from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)
                    return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username Or password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    user1 = User.objects.get(id=request.user.id)
    if(Recipe.objects.filter(user=request.user).count()==0):
        with open('recipes.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter="w",)
         for row in spamreader:
             id = row[0]
             recipeTitle = row[1]
             cookTime = row[2]
             ingredients = row[3]
             recipeLink = row[4]
             recipeImages = row[5]
             Recipe(user = user1, id = id, recipeTitle = recipeTitle, cookTime = cookTime, ingredients = ingredients, recipeLink = recipeLink, recipeImages = recipeImages, saved = False).save()
    return render(request,"Home/Home.html")
