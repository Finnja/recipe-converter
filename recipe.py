from ingredient import *
import re
import json
import requests as r
from bs4 import BeautifulSoup



class recipe(object):
	"""docstring for recipe"""
	def __init__(self, url):
		super(recipe, self).__init__()
		self.url = url
	
	def scrape(self):
		html = r.get(self.url).text
		soup = BeautifulSoup(html)

		ingredients_raw = soup.find_all('span', attrs={'class': 'recipe-ingred_txt'})
		ingredients_raw = ingredients_raw[:-3]
		ingredients_raw = [ingredient.getText() for ingredient in ingredients_raw]
		self.ingredients_raw = ingredients_raw

		directions_raw = soup.find_all('span', attrs={'class': 'recipe-directions__list--item'})
		directions_raw = directions_raw[:-1]
		directions_raw = [step.getText() for step in directions_raw]
		self.directions_raw = directions_raw

	def parseIngredients(self):
		measurements = ['tablespoon', 'tablespoons', 'teaspoon', 'teaspoons', 'cup', 'cups', 'ounce',
					'ounces', 'pound', 'pounds', 'clove', 'cloves', 'dash',
					'slice', 'slices', 'stalk', 'stalks', 'can', 'cans', 'package', 'packages',
					'quart', 'quarts', 'bag', 'bags', 'packet', 'packets', 'envelope', 'envelopes',
					'bottle', 'bottles']

		descriptors = ['fresh', 'freshly', 'extra virgin', 'unsalted', 'salted', 'dried', 'ground',
						'kosher', 'whole', 'dry', 'all-purpose', 'distilled', 'cold',
						'skinless', 'boneless', 'small', 'large', 'frozen', 'low-sodium', 'reduced-fat',
						'low-fat', 'lean']

		preparations = ['sliced', 'chopped', 'crushed', 'grated', 'toasted', 'peeled',
						'deveined', 'juiced', 'minced', 'diced', 'drained', 'beaten',
						'melted', 'divided', 'shredded', 'cored', 'halved', 'quartered']

		ingredients_parsed = []

		for i in self.ingredients_raw:
			measurement = []
			descriptor = []
			preparation = []
			quantity = None

			i = re.sub("[\(\[].*?[\)\]]", "", i)

			i = i.split(' ')

			to_remove = []

			for word in i:
				
				strip_word = re.sub(',', '', word)
				
				# add multi-word fraction support
				if hasNumbers(word):
					quantity = word
					to_remove.append(word)

				if word in measurements:
					measurement = word
					to_remove.append(word)

				if strip_word in preparations:
					preparation.append(strip_word)
					to_remove.append(word)

				if strip_word in descriptors:
					descriptor.append(strip_word)
					to_remove.append(word)

			for r in to_remove:
				i.remove(r)
			
			# recreate whole string
			i = ' '.join(i)

			# 'to taste' special case
			if (quantity is None) and ('to taste' in i):
				i = i.replace('to taste', '')
				quantity = 'to taste'

			if ',' in i:
				i = i.split(',')[0]

			if ' - ' in i:
				i = i.split('-')[0] 

			ing = ingredient(i, quantity, measurement, descriptor, preparation)
			ingredients_parsed.append(ing)

		self.ingredients = ingredients_parsed

if __name__ == '__main__':
	test = recipe('http://allrecipes.com/recipe/176132/slow-cooker-buffalo-chicken-sandwiches/')
	test.scrape()
	test.parseIngredients()
	for ing in test.ingredients:
		x = json.dumps(ing.__dict__)
		print x
			