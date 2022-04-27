from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.
# Views define how the html page will render and look. they use data from the model


@login_required(login_url='login')
def dashboard(request):
    fridges = Fridge.objects.all()
    ingredients = Ingredient.objects.all()
    return render(request, 'accounts/dashboard.html', {'fridges':fridges, 'ingredients':ingredients})