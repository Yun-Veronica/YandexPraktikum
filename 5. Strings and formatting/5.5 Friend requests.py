'''
Задача 1.
Это код Анфисы, который вы последовательно писали на протяжении нескольких тем.
Можете запустить его, вспомнить как выполняются запросы из списка queries.
А. Отредактируйте список запросов queries. Все запросы должны начинаться с обращения Анфиса:
    Анфиса, сколько у меня друзей?
    Анфиса, кто все мои друзья?
    Анфиса, где все мои друзья?
    Анфиса, кто виноват?
Б. Напишите функцию process_query(query). Значение параметра query должно быть обработано методом split().
Отделите имя в начале от тела запроса (т.е. от оставшейся части).
Если запрос начинается с имени «Анфиса», то вызовите функцию process_anfisa(), передав в неё тело запроса как параметр.
И верните результат выполнения этой функции.
Если запрос начинается с другого имени, то пока ничего не делайте — это отложим до следующей задачи.
В. Измените в функции runner() вызов process_anfisa() на вызов process_query().
'''

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_query(query):
    new_query = query.split(', ')
    if 'Анфиса' in new_query:
        return process_anfisa(new_query[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


runner()

'''
Задача 2.
А. Напишите функцию process_friend(name, query), принимающую имя друга name и запрос query.
Если друга с указанным именем 'Н' нет в списке, то функция должна вернуть сообщение об ошибке :
'У тебя нет друга по имени Н'.
Если запрос — «ты где?», то функция должна вернуть сообщения 'Н в городе Г', где Г определяется по данным словаря DATABASE.
Если запрос не «ты где?», а какой-то другой, то функция должна вернуть сообщение об ошибке <неизвестный запрос>.
Б. Допишите функцию process_query(). Если запрос начинается не с «Анфиса», а с другого имени, 
то вызовите функцию process_friend(name, query), передав в неё имя друга и тело запроса. 
И верните результат выполнения этой функции.
В. Добавьте в список queries новые запросы вида:
Коля, ты где?
Соня, что делать?
Антон, ты где?
'''

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name not in DATABASE.keys():
        return f'У тебя нет друга по имени {name}'
    elif query == 'ты где?':
        return f'{name} в городе {DATABASE[name]}'
    else:
        return '<неизвестный запрос>'


def process_query(query):
    new_query = query.split(', ')
    if 'Анфиса' in new_query:
        return process_anfisa(new_query[1])
    else:
        return process_friend(new_query[0], new_query[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


runner()
