from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from Home.models import Recipe
from django.contrib.auth.models import User
# Create your views here.

def Popular(request):
    recipes = Recipe.objects.all()
    context = {
        'Recipes' : recipes,
    }
    return render(request,"Popular/Popular.html", context)
