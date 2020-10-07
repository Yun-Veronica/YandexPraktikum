'''
Задача
Допишите код функции print_friends_count(), добавьте аргумент name со значением по умолчанию.
Если вы при вызове передаёте функции имя, она должна вывести на экран строку вида '{имя}, у тебя N друзей',
если нет — тогда просто 'У тебя N друзей'.
'''


def print_friends_count(friends_count, name=''):  # добавьте новый аргумент
    if friends_count == 1:
        text = '1 друг'
    elif 2 <= friends_count <= 4:
        text = str(friends_count) + ' друга'
    elif friends_count >= 5:
        text = str(friends_count) + ' друзей'
    if name:
        print(f'{name}, у тебя {text}')
    else:
        print(f'У тебя {text}')


# дальше код не меняйте
print_friends_count(3, 'Артём')
print_friends_count(friends_count=7, name='Марина')
print_friends_count(6)
print_friends_count(4, name='Настя')
