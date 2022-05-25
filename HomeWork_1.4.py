# Написать программу получающую набор произведений чисел от 1 до N.
# Пример, пусть N=4, тогда [1,2,6,24]
from re import I
from tkinter import N

print('Задайте число N')
N = int(input(''))

numbers = [(i + 1) for i in range(N)]
print(numbers)
digit=1
k=1
for k in range(len(numbers)):
    old_digit=digit
    digit=digit*numbers[k]
    k+=1
print(digit)
