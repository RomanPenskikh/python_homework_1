# Пользователь задает две строки. Определить количество вхождений одной строки в другую
from cgitb import text

from certifi import where


print('Задайте строку №1')
a = input('')
print('Задайте строку №2 для проверки вхождения в строку №1')
b = input('')


def string(text1, text2):
    count = 0
    i = 0
    while i != -1:
        i = text1.find(text2, i+1)
        count = count + 1
        return count


print(f"{string(a,b)}")

