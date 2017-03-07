import re

class ingredient(object):
	"""docstring for ingredient"""
	def __init__(self, name, quant, measurement, descripts, preps):
		super(ingredient, self).__init__()
		self.name = name
		self.quantity = quant
		self.measurement = measurement
		self.descriptors = descripts
		self.preparations = preps


def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

# if __name__ == '__main__':
# 	il = scrape('http://allrecipes.com/recipe/176132/slow-cooker-buffalo-chicken-sandwiches')



	