__author__ = 'Ablezgov Andrew'

# Задача: Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в
# последнюю ячейку строки. В конце следует вывести полученную матрицу.

LIST = []

for i in range(4):
    row = []
    s = 0
    for j in range(4):
        n = int(input('Введите значение: '))
        row.append(n)
        s += n
    row.append(s)
    LIST.append(row)

for i in LIST:
    print(i)

