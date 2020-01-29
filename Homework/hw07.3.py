
# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import timeit
from random import randint
from statistics import median


def find_median(orig_list):

    for i in range(len(orig_list)):
        idx_min = i
        sort_check = False
        for j in range(i + 1, len(orig_list)):
            if orig_list[j] < orig_list[idx_min]:
                idx_min = j
                sort_check = True
        if sort_check:
            tmp = orig_list[idx_min]
            orig_list[idx_min] = orig_list[i]
            orig_list[i] = tmp

    return orig_list


m = int(input('Введите значение числа m: '))
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Изначальный массив: {orig_list}')
print(f'Тестовая проверка через модуль Statistics: {median(orig_list)}')

find_median(orig_list)
print(f'Медиана отсортированного массива: {orig_list} равна {orig_list[m]}')
# замеры m = 1000
print(timeit.timeit("find_median(orig_list)", setup="from __main__ import find_median, orig_list", number=1000))
# 3.753571 мс

