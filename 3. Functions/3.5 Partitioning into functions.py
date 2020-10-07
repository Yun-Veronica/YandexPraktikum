'''
Задача 1.
Подготовьте код Анфисы к использованию на сервере.
Напишите функцию process_query(). Перенесите в неё весь код из тела основной программы. Эта функция будет принимать на вход запросы пользователя и выдавать ответ на них. Пока она может обработать всего один запрос — сообщить количество друзей.
Добавьте вызов функции process_query() в тело основной программы.
'''

FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']


def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


# перенесите в функцию process_query() вот этот код:
def process_query():
    print("Привет, я Анфиса!")
    count = len(FRIENDS)
    print_friends_count(count)


process_query()

'''
Задача 2.
На серверы приходит множество запросов — от разных пользователей или от других серверов. 
Измените функцию process_query() (обработчик запроса), чтобы она поддерживала несколько разных запросов, а не только один.
Добавьте аргумент query в функцию process_query(). Этот аргумент будет сообщать, какой именно запрос необходимо обработать.
В начало функции process_query() добавьте проверку значения переменной query:
если значение равно 'Сколько у меня друзей?' — выведите ответ на этот вопрос, как в предыдущем задании;
в противном случае — выведите '<неизвестный запрос>';
Анфиса должна здороваться при любом запросе.
Добавьте вызов process_query('Сколько у меня друзей?') в основное тело программы.
Добавьте ещё один вызов process_query('Как меня зовут?') в основное тело программы.
'''

FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']


def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


# перенесите в функцию process_query() вот этот код:
def process_query(query):
    print("Привет, я Анфиса!")
    if query == 'Сколько у меня друзей?':
        count = len(FRIENDS)
        print_friends_count(count)
    else:
        print('<неизвестный запрос>')


process_query('Сколько у меня друзей?')
process_query('Как меня зовут?')

'''
Задача 3.
Добавьте в функцию process_query() обработку ещё одного запроса 'Кто все мои друзья?'. 
В ответ нужно выводить на экран Твои друзья: {список_друзей}, где {список_друзей} — строка, состоящая из списка друзей, 
разделённых запятой и пробелом.
Добавьте вызов process_query('Кто все мои друзья?') в тело основной программы.
'''

FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']


def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


# перенесите в функцию process_query() вот этот код:
def process_query(query):
    print("Привет, я Анфиса!")
    if query == 'Сколько у меня друзей?':
        count = len(FRIENDS)
        print_friends_count(count)
    elif query == 'Кто все мои друзья?':
        print(f'Твои друзья:', ', '.join(FRIENDS))
    else:
        print('<неизвестный запрос>')


process_query('Сколько у меня друзей?')
process_query('Как меня зовут?')
process_query('Кто все мои друзья?')
