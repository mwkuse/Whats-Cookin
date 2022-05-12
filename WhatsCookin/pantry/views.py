from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Home.models import Recipe
from .models import *

# Create your views here.
# Views define how the html page will render and look. they use data from the model
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

@login_required(login_url='login')
def dashboard(request):
    fridges = Fridge.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'pantry/dashboard.html', {'fridges':fridges, 'ingredients':ingredients})

@login_required(login_url='login')
def fridgeFill(request):
    return render(request, 'pantry/fridgeFill.html')
