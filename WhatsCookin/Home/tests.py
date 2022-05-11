from django.test import TestCase
from Home.models import Recipe
from django.contrib.auth.models import User
# Create your tests here.

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='azsxdc12345')
        login = self.client.login(username='testuser', password='azsxdc12345')
        ingredients = ['steak','chicken','salt','pepper','gravy']
        Recipe.objects.create(user = self.user, id = 0, recipeTitle = 'chicken steak', cookTime = 120 , ingredients = ingredients, recipeLink = 'www.link.com', recipeImages = 'picture', saved = False)

    def smoke_test(self):
        self.assertTrue(True)

    def test_ingredients(self):
        recipe = Recipe.objects.get(id=0)
        self.assertTrue(recipe.ingredients, ['steak','chicken','salt','pepper','gravy'])

    def test_saved(self):
        recipe = Recipe.objects.get(id=0)
        self.assertEqual(recipe.saved, False)
