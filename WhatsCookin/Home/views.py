from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def Home(request):
        return render(request,"Home/Home.html")
