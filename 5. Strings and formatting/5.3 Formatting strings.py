'''
Задача 1.
Замените объединение строк на f-строку.
'''


def show_meteo(temperature, weather):
    print(f'Сейчас {weather}, на градуснике {temperature}.')


show_meteo(24, 'облачно')

'''
Задача 2.
В коде задачи из темы «Циклы и ветвления» замените все объединения строк на f-строки.
'''


def format_text(messages_count):
    remainder = messages_count % 10
    if messages_count == 0:
        return 'нет новых сообщений'
    elif remainder == 0 or remainder >= 5 or (10 <= messages_count <= 19):
        return f'{messages_count} новых сообщений'
    elif remainder == 1:
        return f'{messages_count} новое сообщение'
    else:
        return f'{messages_count} новых сообщения'


def print_count(messages_count):
    text = format_text(messages_count)
    print(f'У вас {text}.')


print_count(0)
print_count(1)
print_count(4)
print_count(5)
print_count(12)
print_count(22)
print_count(25)
