'''
Задача
У вас есть запрос «как стать бэкенд-разработчиком».
Соберите URL страницы, на которой Яндекс покажет результаты поиска по этому запросу.
'''

user_query = 'как стать бэкенд-разработчиком'

url = f'https://yandex.ru/search/?text=' + '%20'.join(user_query.split(' '))

print(url)
