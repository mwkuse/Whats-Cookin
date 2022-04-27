from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class Recipe(models.MODEL):
    id = models.IntegerField(primary_key = True)
    recipeTitle = models.CharField(max_length = 200)
    cookTime = models.IntegerField()
    ingredients = models.ListCharField(base_field=CharField(max_length=50), size=20, max_length=(20 * 50),)
    recipeLink = models.CharField(max_length = 500)
    recipeImages = models.CharField(max_length = 500)
