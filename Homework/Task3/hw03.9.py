
# Задача: Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint

N = 5
LIST = []

for i in range(N):
    row = []
    for j in range(N):
        row.append(randint(0, 9))
    LIST.append(row)

print('Задана матрица:')
for i in LIST:
    print(i)

LIST_MIN = []
for i in range(N):
    m = LIST[0][i]
    for j in range(1, N):
        if LIST[j][i] < m:
            m = LIST[j][i]
    LIST_MIN.append(m)

MAX_NUMB = LIST_MIN[0]
for i in range(1, len(LIST_MIN)):
    if LIST_MIN[i] > MAX_NUMB:
        MAX_NUMB = LIST_MIN[i]
print(f'\nМаксимальное значение среди минимальных элементов столбцов матрицы: {MAX_NUMB}')
