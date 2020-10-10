'''
Задача
На прошлом уроке вы заказывали страницу на русском языке через параметры в URL.
Сейчас сделайте то же самое, только русский язык запрашивайте через заголовок запроса 'Accept-Language'.
'''

import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    'Accept-Language':'ru'
}

# не забудьте передать параметры и заголовки в http-запрос через аргументы `params` и `headers` функции get()
response =requests.get(url, params=weather_parameters,headers=request_headers )
print(response.text)