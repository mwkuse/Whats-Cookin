from django.db import models
from django_mysql.models import ListCharField
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    id = models.IntegerField(primary_key = True)
    recipeTitle = models.CharField(max_length = 200)
    cookTime = models.IntegerField()
    ingredients = ListCharField(base_field=models.CharField(max_length=45), size=20, max_length=(20 * 50),)
    recipeLink = models.CharField(max_length = 500)
    recipeImages = models.CharField(max_length = 500)
    favorite = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.recipeTitle
