from django.test import TestCase
from Home.models import Recipe
from django.contrib.auth.models import User
# Create your tests here.


#test search bar?

class SearchTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='azsxdc12345')
        login = self.client.login(username='testuser', password='azsxdc12345')
        ingredients = ['steak','chicken','salt','pepper','gravy']
        Recipe.objects.create(id = 0, recipeTitle = 'chicken steak', cookTime = 120 , ingredients = ingredients, recipeLink = 'www.link.com', recipeImages = 'picture')

    def test_english(self):
        query="ch1cken"
        user_recipes = Recipe.objects.all()
        search_recipes = user_recipes.filter(recipeTitle__icontains = query)
        self.assertEqual(search_recipes.exists(), False)

    def test_correct(self):
        query="chicken"
        user_recipes = Recipe.objects.all()
        search_recipes = user_recipes.filter(recipeTitle__icontains = query)
        self.assertEqual(search_recipes.exists(), True)

    def test_empty(self):
        query = ""
        user_recipes = Recipe.objects.all()
        search_recipes = user_recipes.filter(recipeTitle__icontains = query)
        self.assertEqual(search_recipes.exists(), True)
