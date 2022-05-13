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
        search_recipes = Recipe.objects.all().filter(recipeTitle__icontains = query)
        context = {
            'Recipes' : search_recipes,
        }
    else:
        context = {
            'Recipes:': [],
        }
    return render(request,"Edamam/recipe.html", context)
