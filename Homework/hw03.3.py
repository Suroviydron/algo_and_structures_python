__author__ = 'Ablezgov Andrew'

# Задача: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

N = 10
LIST = []

while N > 0:
    LIST.append(randint(0, 100))
    N -= 1
print(f'Сгенерировался массив случайных чисел: {LIST}')

MIN_NUMB = LIST[0]
MAX_NUMB = LIST[0]
MIN_INDEX = 0
MAX_INDEX = 0

for i, j in enumerate(LIST[1:]):
    if j < MIN_NUMB:
        MIN_NUMB = j
        MIN_INDEX = i + 1
    if j > MAX_NUMB:
        MAX_NUMB = j
        MAX_INDEX = i + 1

print(f'Минимальное значение массива: {MIN_NUMB}\nМаксимальное значение массива: {MAX_NUMB}')

LIST[MIN_INDEX], LIST[MAX_INDEX] = LIST[MAX_INDEX], LIST[MIN_INDEX]

print(f'Меняю значения местами...\nИтоговый вариант массива: {LIST}')
