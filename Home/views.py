from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Home.models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your views here.

@login_required(login_url='login')
def Home(request):
    recipes = Recipe.objects.all()
    context = {
        'Recipes' : recipes,
    }
    return render(request,"Home/Home.html",context)

@login_required(login_url='login')
def Saved(request,id):
    if(request.method == 'GET'):
        recipe = Recipe.objects.get(id=id)
        if(request.user not in recipe.favorite.all()):
            print("here")
            recipe.favorite.add(request.user)
        else:
            print("nothere")
            recipe.favorite.remove(request.user)
        recipes = Recipe.objects.all()
        context = {
            'Recipes' : recipes,
        }
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'),context)
