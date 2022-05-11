from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Home.models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your views here.

def Home(request):
    recipes = Recipe.objects.all()
    context = {
        'Recipes' : recipes,
    }
    return render(request,"Home/Home.html",context)

def Saved(request,id):
    if(request.method == 'GET'):
        recipe = Recipe.objects.get(id=id)
        if(recipe.saved==False):
            recipe.saved = True
            recipe.save()
        else:
            recipe.saved = False
            recipe.save()
        recipes = Recipe.objects.filter(user=request.user)
        context = {
            'Recipes' : recipes,
        }
    return render(request,"Home/Home.html",context)
