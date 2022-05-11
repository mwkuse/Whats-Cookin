from recipe_scrapers import scrape_me
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from parse_ingredients import parse_ingredient
import pandas


mainCategories = ['https://www.allrecipes.com/recipes/17562/dinner/',
'https://www.allrecipes.com/recipes/78/breakfast-and-brunch/',
'https://www.allrecipes.com/recipes/17561/lunch/',
'https://www.allrecipes.com/recipes/76/appetizers-and-snacks/',
'https://www.allrecipes.com/recipes/156/bread/',
'https://www.allrecipes.com/recipes/79/desserts/',
'https://www.allrecipes.com/recipes/77/drinks/',
'https://www.allrecipes.com/recipes/80/main-dish/',
'https://www.allrecipes.com/recipes/96/salad/',
'https://www.allrecipes.com/recipes/81/side-dish/',
'https://www.allrecipes.com/recipes/94/soups-stews-and-chili/']

title = []
time = []
link = []
ingredients = []
image = []

def getFirstPageData(page):
    html = urlopen(page)
    soup = BeautifulSoup(html, 'lxml')
    for i in soup.find_all('a', class_="card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom"):
        if(re.search('\/recipe\/',i.get('href'))):
            betteringredient = []
            scraper = scrape_me(i.get('href'))
            if(i.get('href') not in link):
                title.append(scraper.title())
                time.append(scraper.total_time())
                link.append(i.get('href'))
                for k in scraper.ingredients():
                    betteringredient.append(parse_ingredient(k).name)
                ingredients.append(betteringredient)
                image.append(scraper.image())



def getPageData(page):
    html = urlopen(page)
    soup = BeautifulSoup(html, 'lxml')
    #print(soup)
    for i in soup.find_all('a', class_="tout__titleLink elementFont__toutLink"):
        if(re.search('\/recipe\/',i.get('href'))):
            #print('https://www.allrecipes.com'+i.get('href'))
            scraper = scrape_me(i.get('href'))
            #print(scraper.title())
            title.append(scraper.title())
            time.append(scraper.total_time())
            link.append(i.get('href'))
            ingredients.append(scraper.ingredients())
            image.append(scraper.image())

count = 2
for k in mainCategories:
    getFirstPageData(k)
    #recipe_dict = {'Title': title, 'Time': time, 'Ingredients': ingredients, 'Link': link, 'Image': image}
    #print(recipe_dict)
    #data_frame = pandas.DataFrame(recipe_dict)
    #data_frame.to_csv('recipes.csv','w')

#for j in mainCategories:
#    newpage = j + '?page='+ str(count)
#    response = requests.get(str(newpage))
#    while response.status_code != 400:
#        print(newpage)
#        getPageData(newpage)
#        count+=1
#        newpage = j + '?page='+ str(count)
#        response = requests.get(str(newpage))
#    count = 1
    #print(newpage)
recipe_dict = {'Title': title, 'Time': time, 'Ingredients': ingredients, 'Link': link, 'Image': image}
data_frame = pandas.DataFrame(recipe_dict)
data_frame.to_csv('recipes.csv','w')
