'''
Задача 1.
Научим Анфису хранить в словаре записи о друзьях и получать к ним доступ по ключу.
Напечатайте на экран город, в котором живёт Серёга.
'''

friends = {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск'}
print(friends['Серёга'])  # ваш код здесь

'''
Задача 2.
Серёга переехал в Оренбург. Получив по ключу доступ к записи о его городе, отразите этот факт в словаре.
'''

friends = {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск'}

# ваш код здесь
friends['Серёга'] = 'Оренбург'

print('Серёга теперь живёт в славном городе ' + friends['Серёга'])
