'''
Задача 1.
Научите Анфису сообщать пользователю, сколько времени шёл его любимый сериал.
Дата выхода первой серии - 17 апреля 2011 года.
Дата выхода последней серии - 15 апреля 2019 года.
'''

import datetime as dt

start_time = dt.datetime(2011, 4, 17)  # дата выхода первой серии
final_time = dt.datetime(2019, 4, 15)  # впишите дату выхода последней серии

duration = final_time - start_time  # вычислите, сколько времени шёл сериал

print(duration)

'''
Задача 2.
Напишите код, отвечающий на запрос пользователя Сколько времени у меня уже ушло на вводный курс по бэкенд-разработке?
Вспомните, в какой день и во сколько вы начали проходить курс. Запишите этот момент времени в переменную start_moment. 
В переменную current_moment запишите текущий момент времени. 
Затем вычислите разницу двух этих моментов, запишите её в переменную total_time, и напечатайте её на экране.
'''

import datetime as dt

start_moment = dt.datetime(2020, 10, 5)  # напишите код здесь
current_moment = dt.datetime(2020, 10, 9)  # напишите код здесь

total_time = current_moment - start_moment  # и здесь

print(total_time)
