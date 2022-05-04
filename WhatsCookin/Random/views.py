from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from Home.models import Recipe
import re
# Create your views here.

def Random(request):
    recipes = Recipe.objects.all()
    ingredient = []
    for i in recipes:
        for j in i.ingredients:
            print(j.split('"'))
    context = {
        'Recipes' : recipes,
        'ingredient' : ingredient,
    }
    return render(request,"Random/Random.html", context)
