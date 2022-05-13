from django.test import TestCase
from Home.models import Recipe
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='azsxdc12345')
        login = self.client.login(username='testuser', password='azsxdc12345')
        ingredients = ['steak','chicken','salt','pepper','gravy']
        Recipe.objects.create(id = 0, recipeTitle = 'chicken steak', cookTime = 120 , ingredients = ingredients, recipeLink = 'www.link.com', recipeImages = 'picture')
        Recipe.objects.create(id = 1, recipeTitle = 'chicken steak', cookTime = 120 , ingredients = ingredients, recipeLink = 'www.link.com', recipeImages = 'picture')


    def smoke_test(self):
        self.assertTrue(True)

    def test_Ingredients(self):
        recipe = Recipe.objects.get(id=0)
        self.assertTrue(recipe.ingredients, ['steak','chicken','salt','pepper','gravy'])

    def test_Favorited(self):
        recipe = Recipe.objects.get(id=0)
        self.assertEqual(recipe.favorite.count(),0)
        user = self.user
        recipe.favorite.set([user])
        self.assertEqual(recipe.favorite.count(),1)
        recipe.favorite.set([])
        self.assertEqual(recipe.favorite.count(),0)

    def test_model_String(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), "chicken steak")
