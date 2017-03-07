
ing_list = ['chicken', 'salt', 'bread crumbs', 'oil']
h = {'salt':'garlic powder'}
v = {'chicken':'seitan'}
gf = {'bread crumbs':'ground flaxseeds'}
asian = {'wine':'rice wine',
    'cooking oil':'sesame oil', 
    'oil':'sesame oil', 
    'mozzerella':'rushan',
    'mozzerella cheese':'rushan',
    'cheddar cheese' : 'rushan',
    'cheddar' : 'rushan',
    'blue cheese': 'rushan',
    'parmesan': 'rushan',
    'parmesan cheese': 'rushan',
    'romano' : 'rushan',
    'romano cheese' : 'rushan',
    'gouda' : 'rushan',
    'gouda cheese' : 'rushan',
    'swiss': 'rushan',
    'swiss cheese': 'rushan',
    'cheddar' : 'rushan',
    'cheddar cheese' : 'rushan',
    'provolone' : 'rushan',
    'provolone cheese' : 'rushan',
    'feta': 'rushan',
    'feta cheese': 'rushan',
    'cream cheese' : 'rubing',
    'yogurt' : 'nai lao',
    'gravy' : 'chinese brown gravy',
    'sausage':'chicken',
    'anchovies' : 'shrimp',
    'bacon' : 'salted pork',
    'okra' : 'bok choy',
    'asparagus' : 'bok choy',
    'squash' : 'choy sum',
    'corn' : 'baby corn',
    'refried beans' : 'green beans',
    'chick peas' : 'peking chick peas',
    'butternut squash' : 'oriental squash',
    'lettuce' : 'bok choy',
    'broccoli' : 'kai-lan',
    'blueberries' : 'chinese blueberries',
    'watermelon' : 'wax gourd',
    'arugula' : 'chinese cabbage',
    'olives' : 'chinese olives',
    'spaghetti squash' : 'string beans',
    'penne pasta' : 'noodles',
    'spaghetti' :'noodles',
    'macaroni': 'rice',
    'elbow pasta' : 'rice',
    'pasta' :'rice',
    'olive oil': 'peanut oil',
    'jalapeno' : 'red or green chili',
    'tobasco': 'sriracha',
    'hot sauce': 'sriracha',
    'habanero pepper' : 'red or green chili',
    }



def recipe_transform(ingredients):
    transformation = raw_input('Choose a transformation (h = healthy, v = vegetarian, gf = gluten free, asian = Asian): ')

    if transformation == 'h':
        count = 0
        for i in ingredients:
            new_ing = h.get(i,i)
            ingredients[count] = new_ing
            count += 1
        print ingredients
    elif transformation == 'v':
        count = 0
        for i in ingredients:
            new_ing = v.get(i,i)
            ingredients[count] = new_ing
            count += 1
        print ingredients
    elif transformation == 'gf':
        count = 0
        for i in ingredients:
            new_ing = gf.get(i,i)
            ingredients[count] = new_ing
            count += 1
        print ingredients
    elif transformation == 'asian':
        count = 0
        for i in ingredients:
            new_ing = asian.get(i,i)
            ingredients[count] = new_ing
            count += 1
        print ingredients
    else:
        print('Please enter a valid transformation type')
        recipe_transform(ing_list)

recipe_transform(ing_list)
    


