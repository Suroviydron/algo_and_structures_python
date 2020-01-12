__author__ = 'Ablezgov Andrew'

# Задача-4: Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

from random import random

LEFT_BOARD = int(input('Введите минимальное значение: '))
RIGHT_BOARD = int(input('Введите максимальное значение: '))

RESULT = int(random() * (RIGHT_BOARD - LEFT_BOARD + 1) + LEFT_BOARD)
print(f'Случайное число в указанном Вами диапозоне: {RESULT}')

LEFT_BOARD = ord(input('\nЗадайте диапозон для поиска случайного символа. \nМинимальный: '))
RIGHT_BOARD = ord(input('Максимальный: '))
RESULT = int(random() * (RIGHT_BOARD - LEFT_BOARD + 1) + LEFT_BOARD)
print(f'Случайное число в указанном Вами диапозоне: {chr(RESULT)}')

