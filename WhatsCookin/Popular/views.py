from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title = "What's Cookin"
    content = "Hello Team"
    context = {
        "title":title,
        "body":content
    }
    return render(request, "index.html", context = context)
