from pprint import pprint

cook_book = {}
with open('recipe_book.txt', encoding='utf8') as file_recipes:
    all_lines = file_recipes.readlines()
    number_dishes = len([l for l in all_lines if l == '\n']) + 1
with open('recipe_book.txt', encoding='utf8') as file_recipes:
    for id in range(number_dishes):
        while True:
            line = file_recipes.readline().rstrip('\n')
            if not line:
                break
            cook_book[line] = []
            number_ingredients = int(file_recipes.readline().rstrip('\n'))
            ingredients = [file_recipes.readline().rstrip('\n').split('|') for i in range(number_ingredients)]
            for ingredient in ingredients:
                new_values = [ingredient[0].rstrip(' '), int(ingredient[1]), ingredient[2].replace(' ', '')]
                new_key = ['ingredient_name', 'quantity', 'measure']
                cook_book[line].append(dict(zip(new_key, new_values)))

def get_shop_list_by_dishes(dishes=[], person_count=int):
    new_shop_list = {}
    for dishe in dishes:
        for name_dishes, ingredients in cook_book.items():
            if dishe in name_dishes:
                for ingredient in ingredients:
                    ingredient['quantity'] *= person_count
                    new_key = ingredient['ingredient_name']
                    ingredient.pop('ingredient_name')
                    if new_key not in new_shop_list:
                        new_shop_list[new_key] = ingredient
                    else:
                        new_shop_list[new_key]['quantity'] += new_shop_list[new_key]['quantity']
    return new_shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

