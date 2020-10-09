'''
Задача 1.
Если вы захотите научить Анфису играть в города, ей нужно будет уметь выбирать город из множества городов, которые она знает, исключая те, что уже были названы.
Напишите функцию print_valid_cities, которая сравнит множество всех городов all_cities со множеством названных городов used_cities и:
создаст множество городов, которые ещё можно использовать,
напечатает такое множество на экран, разделяя города запятой.
Запустите эту функцию на примерах разных множеств и посмотрите, как она работает.
'''


def print_valid_cities(all_cities, used_cities):
    return set(set.difference(all_cities, used_cities))


all_cities = set(['Абакан', 'Астрахань', 'Бобруйск', 'Калуга', 'Караганда', 'Кострома', 'Липецк', 'Новосибирск'])

used_cities = set(['Калуга', 'Абакан', 'Новосибирск'])

print(', '.join(print_valid_cities(all_cities, used_cities)))

'''
Задача 2.
Научите Анфису помогать вам с покупками в магазине.
Вы хотите приготовить два блюда и рассказываете Анфисе, какие для них нужны продукты.
Напишите функцию print_shopping_list(), которая будет получать два списка продуктов —recipe1 и recipe2, 
и печатать на экран полный список покупок.
Элементы в списке не должны повторяться и должны быть выведены через запятую, 
в формате обычной текстовой строки (без фигурных скобок).
'''


def print_shopping_list(recipe1, recipe2):  # напишите здесь свою функцию
    return set.union(set(recipe1), set(recipe2))


pizza = ['мука', 'помидоры', 'шампиньоны', 'сыр', 'оливковое масло']
salad = ['огурцы', 'перцы', 'помидоры', 'оливковое масло', 'листья салата']

print(', '.join(print_shopping_list(pizza, salad)))

'''
Задача 3.
Если вам надо 5 кг помидоров для салата и 3 кг для супа, вы сразу покупаете 8 килограммов.
Напишите функцию, которая напечатает на экран, какие продукты надо купить, и сколько их нужно. 
Информацию о каждом ингредиенте выводите на отдельной строке в формате: огурцы, кг: 1.5.
Каждый продукт должен присутствовать в выводе только один раз.
'''


def print_shopping_list(recipe1, recipe2):
    all_ingridients = set.union(set(recipe1.keys()), set(recipe2.keys()))
    all_needed_products = {}
    for i in all_ingridients:
        if i in recipe1 and i in recipe2:
            all_needed_products.setdefault(i, recipe1[i] + recipe2[i])
        elif i in recipe1:
            all_needed_products.setdefault(i, recipe1[i])
        elif i in recipe2:
            all_needed_products.setdefault(i, recipe2[i])

    return all_needed_products


pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

for k in print_shopping_list(pizza, salad):
    print(f'{k}: {print_shopping_list(pizza, salad)[k]}')