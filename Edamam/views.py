from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Home.models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your views here.

def User_Recipe(request):
    query = request.GET.get("q")
    if query != None and query != "":
        user_recipes = Recipe.objects.all().filter(user = request.user)
        search_recipes = user_recipes.filter(recipeTitle__icontains = query)
        for recipe in search_recipes:
            print(recipe.user)
        context = {
            'Recipes' : search_recipes,
        }
    else:
        context = {
            'Recipes:': [],
        }
    return render(request,"Edamam/recipe.html", context)
