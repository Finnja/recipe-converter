from ingredient import *
from transformation import recipe_transform
import re
import json
import requests as r
import itertools
from bs4 import BeautifulSoup
from fractions import Fraction



class recipe(object):
	"""docstring for recipe"""
	def __init__(self, url):
		super(recipe, self).__init__()
		self.url = url
	
	
	def scrape(self):
		html = r.get(self.url).text
		soup = BeautifulSoup(html, "html.parser")

		ingredients_raw = soup.find_all('span', attrs={'class': 'recipe-ingred_txt'})
		ingredients_raw = ingredients_raw[:-3]
		ingredients_raw = [ingredient.getText() for ingredient in ingredients_raw]
		self.ingredients_raw = ingredients_raw

		directions_raw = soup.find_all('span', attrs={'class': 'recipe-directions__list--item'})
		directions_raw = directions_raw[:-1]
		directions_raw = [step.getText() for step in directions_raw]
		self.directions_raw = directions_raw
		#print self.directions_raw
		

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
						'melted', 'divided', 'shredded', 'cored', 'halved', 'quartered', 'cooked']

		ingredients_parsed = []

		for i in self.ingredients_raw:
			measurement = []
			descriptor = []
			preparation = []
			quantity = []

			i = re.sub("[\(\[].*?[\)\]]", "", i)

			i = i.split(' ')

			to_remove = []

			for word in i:
				
				strip_word = re.sub(',', '', word)
				
				# add multi-word fraction support
				if hasNumbers(word):
					quantity.append(word)
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
			if (len(quantity) == 0) and ('to taste' in i):
				i = i.replace('to taste', '')
				quantity.append('to taste')
			elif len(quantity) > 1:
				quantity = float(sum(Fraction(s) for s in quantity))
			else:
				quantity = float(Fraction(quantity[0]))


			if ',' in i:
				i = i.split(',')[0]

			if ' - ' in i:
				i = i.split('-')[0] 

			ing = ingredient(i, quantity, measurement, descriptor, preparation)
			ingredients_parsed.append(ing)

		self.ingredients = ingredients_parsed

	def findTools(self):
		"""finds tools used in a recipe from list of instructions """
		if not (hasattr(self, 'directions_raw')):
			print('no directions, must run scrape first')
		else:
			#print(self.directions_raw)

			self.tools = []

			tools_master_list = ['baking pan', 'pan', 'baking dish', 'bowl', 'whisk', 'skillet', 'collander', 
						'grater', 'mortar and pestle', 'peeler', 'potatoe masher', 'tongs', 'spoon',
						'saucepan']

			directions_corpus = ' '.join(self.directions_raw)

			for tool in tools_master_list:
				if tool in directions_corpus:
					self.tools.append(tool)

			tools_list = ', '.join(self.tools)
			print 'Tools Needed: ' + tools_list + '\n'
			#print(self.tools)

	def rec_transform(self):
		ing_list = []
		quant = ''
		prep = ''
		desc = ''
		meas = ''
		print 'Ingredients: '
		for i in self.ingredients:
			quant = str(i.quantity)
			desc = ', '.join(i.descriptors)
			prep = ', '.join(i.preparations)
			meas = str(i.measurement)
			print quant + ' ' + meas + ' ' + desc + ' ' + i.name + ' ' +  prep
			ing_list.append(i.name)
		print '\n' + 'Directions: '
		print self.directions_raw
		print '\n'
		transformation = raw_input('Choose a transformation (h = healthy, v = vegetarian, gf = gluten free, asian = Asian, italian = Italian, indian = Indian): ')
		recipe_transform(ing_list, transformation)
		count = 0
		print '\n'
		tools_list = ', '.join(self.tools)
		print 'Tools Needed: ' + tools_list + '\n'
		print 'Ingredients: '
		for i in self.ingredients:
			i.name = ing_list[count]
			quant = str(i.quantity)
			desc = ', '.join(i.descriptors)
			prep = ', '.join(i.preparations)
			meas = str(i.measurement)
			print quant + ' ' + meas + ' ' + desc + ' ' + i.name + ' ' +  prep
			count += 1
		directions_list_raw = []
		directions_list = []
		for direc in self.directions_raw:
			directions_list_raw.append(direc.split())
			directions_list = list(itertools.chain.from_iterable(directions_list_raw))
		recipe_transform(directions_list, transformation)
		#print directions_list
		directions_transformed = ' '.join(directions_list)
		#self.directions = directions_transformed
		print '\n' + 'Directions: '
		print directions_transformed



if __name__ == '__main__':
	test = recipe('http://allrecipes.com/recipe/47397/cashew-avocado-chicken-salad')
	test.scrape()
	test.parseIngredients()
	test.findTools()
	test.rec_transform()
	# for ing in test.ingredients:
	#       x = json.dumps(ing.__dict__)
	#       print x

	#x = json.dumps(test.__dict__)
			
