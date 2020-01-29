
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import timeit
from random import uniform


def merge_sort(orig_list):

    if len(orig_list) > 1:
        left = orig_list[:len(orig_list) // 2]
        right = orig_list[len(orig_list) // 2:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list


orig_list = [round(uniform(0, 49.9), 2) for _ in range(1000)]
print(f'Изначальный массив: {orig_list}')

merge_sort(orig_list)
print(f'Отсортированный массив: {orig_list}')
# замеры 1000
print(timeit.timeit("merge_sort(orig_list)", setup="from __main__ import merge_sort, orig_list", number=1000))
# 3.753571 мс

