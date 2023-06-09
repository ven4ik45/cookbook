from pprint import pprint
# Задание 1
cook_book = {}

with open('files/recipies.txt', 'r') as file:
    for line in file:
        dish = line.strip()
        ingredients_count = int(file.readline().strip())
        ingredients_list = []
        for _ in range(ingredients_count):
            product, count, unit = file.readline().strip().split(' | ')
            ingredients_list.append({
                'ingredient': product,
                'count': int(count),
                'unit': unit
            })
        file.readline()
        cook_book[dish] = ingredients_list
# pprint(cook_book)


# Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = []
    for meal in dishes:
        if check_recipes_in_base(meal):
            for i in cook_book[meal]:
                ingredient = [i['ingredient'], i['count']*person_count, i['unit']]
                if ingredient not in shop_list:
                    shop_list.append(ingredient)
                else:
                    shop_list[shop_list.index(ingredient)][1] += ingredient[1]
    list_to_dict(shop_list)

#Добавил проверку на случай, если нет такого рецепта в книге
def check_recipes_in_base(meal):
    if meal not in cook_book:
        return False
    else:
        return dish


def list_to_dict(shop_list):
    dict_list = {}
    for i in shop_list:
        dict_list[i[0]] = {'measure': i[2], 'quality': i[1]}
    pprint(dict_list)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3)




