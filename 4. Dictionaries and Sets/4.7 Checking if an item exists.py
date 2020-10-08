'''
Задача
Вы собираетесь поехать в Хабаровск. Было бы здорово встретиться там с друзьями.
Но живет ли сейчас хоть кто-то из друзей в Хабаровске?
Научите Анфису отвечать на этот вопрос — сделайте ей функцию is_anyone_in(collection, city)
'''


def is_anyone_in(collection, city):
    if city in collection.values():  # если есть среди значений словаря collection
        for name in collection:  # переберите все ключи словаря
            if city in collection[name]:  # если соответствующее ключу значение равно city
                print('В городе ' + city + ' живёт ' + name + '.')
    else:
        print('Пока никого.')


friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}

is_anyone_in(friends, 'Хабаровск')