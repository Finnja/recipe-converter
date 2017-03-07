
ing_list = ['chicken', 'salt', 'bread crumbs']
h = {'salt':'garlic powder'}
v = {'chicken':'seitan'}
gf = {'bread crumbs':'ground flaxseeds'}


def recipe_transform(ingredients):
    transformation = raw_input('Choose a transformation (h = healthy, v = vegetarian, gf = gluten free): ')

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
    else:
        print('Please enter a valid transformation type')
        recipe_transform(ing_list)

recipe_transform(ing_list)
    


