__author__ = 'Ablezgov Andrew'

# Задача: В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import randint

N = 10
LIST = []

while N > 0:
    LIST.append(randint(0, 100))
    N -= 1
print(f'Сгенерировался массив случайных чисел: {LIST}')

for i in range(len(LIST) - 1):
    for j in range(i + 1, len(LIST)):
        if LIST[i] > LIST[j]:
            LIST[i], LIST[j] = LIST[j], LIST[i]
print(f'Два наименьших элемента сгенерированного массива: {LIST[0:2]}')

