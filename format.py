# -*- coding: utf-8 -*-
from recipe import *
from transformation import recipe_transform
import re
import json
import requests as r
from bs4 import BeautifulSoup
from fractions import Fraction


f = open('results.txt','w') 
test = recipe('http://allrecipes.com/recipe/47397/cashew-avocado-chicken-salad')
test.scrape()
test.parseIngredients()
test.rec_transform()
f.write('INGREDIENTS')
f.write('\n')
for ing in test.ingredients:
	des = ing.descriptors
	meas = ing.measurement
	name = ing.name
	prep = ing.preparations
	quant = ing.quantity
	#quant + measure + prep + des + name
	sentence =  ''
	sentence += str(quant) + ' '
	if len(meas) != 0:
		sentence += meas
	sentence += ' '
	for p in prep:
		sentence += (p + ' ') 
	sentence += ' '
	sentence += name
	f.write(sentence)
	f.write('\n')
 
f.close()