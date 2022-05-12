from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Home.models import Recipe
from .models import *
# Create your views here.
@login_required(login_url='login')
def Pantry(request):
    recipes = Recipe.objects.all()
    ingredient = []
    for i in recipes:
        for j in i.ingredients:
            j = j.replace("'","")
            j = j.lstrip()
            j = j.rstrip()
            print(j)
            if j not in ingredient:
                ingredient.append(str(j))
                print(len(ingredient))
    context = {
        'Ingredients' : ingredient,
    }
    return render(request, "Pantry/Pantry.html", context)
