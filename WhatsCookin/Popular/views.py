from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def Popular(request):
    return render(request,"Popular/Popular.html")
