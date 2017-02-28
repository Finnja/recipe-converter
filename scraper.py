import requests as r
from bs4 import BeautifulSoup


def getIngredients(soup_obj):
	print('ingredients: \n')

	ingredients = soup_obj.find_all('span', attrs={'class': 'recipe-ingred_txt'})
	ingredients = ingredients[:-3]
	for ingredient in ingredients:
		print(ingredient.getText())

def getDirections(soup_obj):
	print('directions: \n')

	directions = soup_obj.find_all('span', attrs={'class': 'recipe-directions__list--item'})
	directions = directions[:-1]
	for step in directions:
		print(step.getText())


def main(url):
	html = r.get(url).text
	soup = BeautifulSoup(html)

	getIngredients(soup)
	print('\n')
	getDirections(soup)

if __name__ == '__main__':
	main('http://allrecipes.com/recipe/9023/baked-teriyaki-chicken')