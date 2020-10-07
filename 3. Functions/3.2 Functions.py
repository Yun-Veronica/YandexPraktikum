'''
Задача 1.
На основе заготовленного кода напишите функцию print_friends_count() для вывода количества друзей.
Аргументом сделайте friends_count.
Вызовите эту функцию не менее трёх раз с разными аргументами от 1 до 20.
'''


def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


print_friends_count(3)
print_friends_count(5)
print_friends_count(1)

'''
Задача 2.
Напишите цикл, в котором функция print_friends_count() вызывается c аргументами от 1 до 10.
Код самой функции не изменяйте.
'''


def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


for i in range(1, 11):
    print_friends_count(i)
