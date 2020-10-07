'''
Задача
Анфиса может анализировать списки.
Например, подсчитывать дни, когда в вашем городе или в городах ваших друзей стояла хорошая погода.
Есть списки средних дневных температур в Москве за май 2017 и 2018 годов.
Создайте функцию comfort_count(temperatures) для подсчёта комфортных дней в переданном списке — дней с температурой воздуха от 22 до 26 градусов включительно.
Функция в результате работы должна вывести на экран строку 'Количество комфортных дней в этом месяце: N',
где N — результат подсчёта в цикле с условием.
Сначала посчитайте комфортные дни в мае 2017-го года, а потом — в мае 2018-го.
'''

may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25,
            17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23,
            18, 22, 23, 11]


# допишите код ниже
def comfort_count(temperatures):
    N = 0
    for temperature in temperatures:
        if 22 <= temperature <= 26:
            N += 1

    print(f'Количество комфортных дней в этом месяце: {N}')


# дальше код не меняйте
comfort_count(may_2017)  # узнаем, что было в мае 2017 г.
comfort_count(may_2018)  # узнаем, что было в мае 2018 г.