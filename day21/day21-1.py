import sys
from collections import defaultdict

allergens_to_foods = defaultdict(list)
all_ingredients = set()
foods = []
for l in open(sys.argv[1]) :
    e = l.split("(")
    if 1 < len(e) :
        allergens=[a[:-1] for a in e[1].split()[1:]]
        ingredients = e[0].split()
        all_ingredients.update(ingredients)
        foods.append((ingredients, allergens))
        for a in allergens :
            allergens_to_foods[a].append(ingredients)

allergens_to_ingredients = {}
for a,fds in allergens_to_foods.items() :
    intersection = {f for f in fds[0]}
    for f in fds[1:]:
        intersection = {i for i in f if i in intersection}
    allergens_to_ingredients[a]=intersection


allergen_to_ingredient = {}
modif = True
while modif :
    modif = False
    to_remove = set()
    for a,ingredients in allergens_to_ingredients.items() :
        if len(ingredients) == 1 :
            allergen_to_ingredient[a]=next(iter(ingredients))
            to_remove.add(a)
    if to_remove :
        modif = True
        for a in to_remove :
            del allergens_to_ingredients[a]
            for allergen, ingredients in allergens_to_ingredients.items() :
                try:
                    ingredients.remove(allergen_to_ingredient[a])
                except KeyError :
                    pass
            all_ingredients.remove(allergen_to_ingredient[a])

print(allergen_to_ingredient)
print(all_ingredients)

count = 0
for ingredient in all_ingredients :
    c = sum(1 for ingredients,allergens in foods if ingredient in ingredients)
    count += c
    print(ingredient, c)
print("total", count)

