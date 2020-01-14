__author__ = 'Ablezgov Andrew'

# Задача: В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

N = 10
LIST = []
NEGAT_LIST = []

while N > 0:
    LIST.append(randint(-20, 20))
    N -= 1
print(f'Сгенерировался массив случайных чисел: {LIST}')

for i in LIST:
    if i < 0:
        NEGAT_LIST.append(i)

if len(NEGAT_LIST) == 0:
    print('В заданном массиве отрицательные элементы отсутствуют')
elif len(NEGAT_LIST) == 1:
    print(f'Максимальный отрицательный элемент сгенерированного массива: {NEGAT_LIST[0]}')
else:
    M = NEGAT_LIST[0]
    for i in NEGAT_LIST[1:]:
        if i > M:
            M = i

    INDEX = 0
    for i, j in enumerate(LIST):
        if j == M:
            INDEX = i + 1
            break

    print(f'Максимальное отрицательное значение массива: {M}\nЕго позиция: {INDEX}')



