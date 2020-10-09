'''
Задача 1.
Научите Анфису сообщать время в формате ЧЧ:ММ:СС (часы, минуты, секунды). Например На часах 19:28:06.
'''


def print_time(hour, minute, second):
    print(f'На часах {hour}:{minute}:{second}')


print_time('19', '28', '06')

'''
Задача 2.
Анфисе передали список listened с хронометражем прослушанных песен в секундах. Выведите на экран суммарную статистику:
'Вы прослушали N песен.'
Где: N — длина списка listened.
'''


def calc_stat(listened):
    # от англ. calculate statistics, посчитать статистику
    # напишите код функции calc_stat
    return f'Вы прослушали {len(listened)} песен.'


print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))

'''
Задача 3.
Анфисе передали список listened (англ. listen, «слушать») с хронометражем прослушанных песен в секундах.
Выведите на экран суммарную статистику:
'Вы прослушали N песен, общей продолжительностью M минут и S секунд.'
Где:
N — длина списка listened;
M — количество целых минут общей продолжительности прослушанного;
S — остаток от целых минут.
'''


def calc_stat(listened):
    # от англ. calculate statistics, посчитать статистику. напишите код функции calc_stat
    N = len(listened)
    M = sum(listened) // 60
    S = sum(listened) % 60
    return f'Вы прослушали {N} песен, общей продолжительностью {M} минут и {S} секунд.'


print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))
