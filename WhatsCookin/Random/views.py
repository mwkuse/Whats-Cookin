from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from Home.models import Recipe
import re
from random import *
# Create your views here.

def Random(request):
    recipes = Recipe.objects.all()
    #print(recipes.count())
    count = 0
    selected = []
    while count < 25:
        id = randrange(recipes.count())
        selected.append(Recipe.objects.get(id=id))
        count+=1

    #code below for us in pantry.
    #ingredient = []
    #for i in recipes:
    #    for j in i.ingredients:
    #        j = j.replace("'","")
    #        j = j.lstrip()
    #        j = j.rstrip()
    #        print(j)
    #        if j not in ingredient:
    #            ingredient.append(str(j))
    #            print(len(ingredient))
    context = {
        'Recipes' : recipes,
        'Selected' : selected,
    }
    return render(request,"Random/Random.html", context)
