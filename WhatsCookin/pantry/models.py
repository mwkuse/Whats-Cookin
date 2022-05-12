from tkinter import TRUE
from django.db import models

# Create your models here.
# A modle is a class that represents a database table


class Ingredient(models.Model):
    name = models.CharField(max_length=100, null = True)
    isSaved = models.BooleanField()

    def __str__(self):
        return self.name

class Fridge(models.Model):
    #date_filled = models.DateTimeField(auto_now_add=True, null = True)
    name = models.CharField(max_length=100, null = True, blank = True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100, null = True)
    phone = models.CharField(max_length=100, null = True)
    email = models.CharField(max_length=100, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    fridges = models.ManyToManyField(Fridge)

    def __str__(self):
        return self.name
