
# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import timeit
import copy
from random import randint
from statistics import median


def find_median(orig_list):

    arr_copy = copy.deepcopy(orig_list)
    for i in range(len(arr_copy)):
        idx_min = i
        sort_check = False
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[j] < arr_copy[idx_min]:
                idx_min = j
                sort_check = True
        if sort_check:
            arr_copy[i], arr_copy[idx_min] = arr_copy[idx_min], arr_copy[i]
    median_number = arr_copy[m]
    del arr_copy
    return median_number


m = int(input('Введите значение числа m: '))
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Изначальный массив: {orig_list}')
print(f'Тестовая проверка через модуль Statistics: {median(orig_list)}')

print(f'Медианное значение через сортировку: {find_median(orig_list)}')

# замеры m = 500
print(timeit.timeit("find_median(orig_list)", setup="from __main__ import find_median, orig_list", number=1000))
# 43.514376600000006 мс

