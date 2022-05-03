import os
import requests

def get_recipes():
    url = 'https://api.edamam.com/api/recipes/v2'
    r = requests.get(url, headers={'hits: ' % 'f2767e05'})
    recipes = r.json()
    recipe_list = []
    for i in range(len(recipes['recipe'])):
        recipe_list.append(recipes['recipe'][i])
    return recipe_list
