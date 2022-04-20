from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def Recipe(request):
    return render(request,"Edamam/recipe.html")
