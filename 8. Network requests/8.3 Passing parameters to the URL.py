'''
Задача 1.
Запросите погодный сервис http://wttr.in по URL без параметров.
А их задайте словарём weather_parameters. Функция get() должна принимать его, как отдельный аргумент params.
'''

import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    'T': ''
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)

'''
Задача 2.
Добавьте в словарь с параметрами weather_parameters ещё два параметра:
M без значения — чтобы скорость ветра была в метрах в секунду, как принято у метеорологов;
lang со значением ru, чтобы прогноз выдавался на русском языке.
Обратите внимание на изменения при добавлении этих параметров. О других параметрах можно прочитать в документации.
'''

import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    'T': '',
    'M': 'm/s',
    'lang': 'ru'
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)
