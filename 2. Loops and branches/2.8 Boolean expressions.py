'''
Задача 1.
Замените три точки в условиях правильным логическим оператором and или or.
'''

for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")

    if current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')
    elif current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')

'''
Задача 2.
Научите Анфису правильно называть количество новых сообщений, когда их меньше 100.
Примените логический оператор or и множественое ветвление с elif, чтобы Анфиса выражалась грамотно.
К примеру: «У вас 1 новое сообщение», «У вас 35 новых сообщений», «У вас 24 новых сообщения».
Последнюю цифру удобнее всего получать как остаток при делении на 10.
В коде этого задания он вычисляется оператором модуло %:
# англ. remainder, «остаток»
remainder = a % 10  # остаток от деления `a` на 10 
'''

# Нужно рассмотреть больше случаев в if-elif-else
for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif remainder == 1 and messages_count != 11:
        print(f'У вас {messages_count} новое сообщение')
    elif remainder in [2, 3, 4] and messages_count not in [12, 13, 14]:
        print(f'У вас {messages_count} новых сообщения')
    else:
        print(f'У вас {messages_count} новых сообщений')
