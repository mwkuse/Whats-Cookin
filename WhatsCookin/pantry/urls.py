from django.urls import path
from . import views

urlpatterns = [
	path('fridgeFill/', views.fridgeFill, name="fridgeFill"),
	
]