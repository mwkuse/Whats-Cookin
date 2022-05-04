from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
# Views define how the html page will render and look. they use data from the model
@login_required(login_url='login')
def Pantry(request):
    return render(request, "Pantry/Pantry.html")

@login_required(login_url='login')
def dashboard(request):
    fridges = Fridge.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'pantry/dashboard.html', {'fridges':fridges, 'ingredients':ingredients})

@login_required(login_url='login')
def fridgeFill(request):
    return render(request, 'pantry/fridgeFill.html')
