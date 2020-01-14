__author__ = 'Ablezgov Andrew'

# Задача: В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

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

SUMM = 0

if MAX_INDEX - MIN_INDEX == 1 or MIN_INDEX - MAX_INDEX == 1:
    print("Минимальный и максимальный элемент находятся на соседних позициях в массиве. "
          "Сумма элементов между ними равна 0")
elif MAX_INDEX > MIN_INDEX:
    for i in LIST[MIN_INDEX + 1:MAX_INDEX]:
        SUMM = SUMM + i
    print(f'Сумма элементов в сгенерированном массиве, находящихся между минимальным и максимальным: {SUMM}')
else:
    for i in LIST[MAX_INDEX + 1:MIN_INDEX]:
        SUMM = SUMM + i
    print(f'Сумма элементов в сгенерированном массиве, находящихся между минимальным и максимальным: {SUMM}')


