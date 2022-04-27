from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Home.models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your views here.

def Home(request):
    recipes = Recipe.objects.order_by("id")[:10]
    context = {
        'Recipes' : recipes,
    }
    return render(request,"Home/Home.html",context)
