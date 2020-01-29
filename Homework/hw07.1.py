
# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть
# реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import timeit
from random import randint


def lazy_bubble(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list


def finished_bubble(orig_list):
    for i in range(len(orig_list) - 1):
        sort_check = True
        for j in range(i+1, len(orig_list)):
            if orig_list[i] < orig_list[j]:
                orig_list[i], orig_list[j] = orig_list[j], orig_list[i]
                sort_check = False
                break
        if sort_check:
            break

    return orig_list


orig_list = [randint(-100, 99) for _ in range(1000)]
print(f'Изначальный массив: {orig_list}')

lazy_bubble(orig_list)
print(f'Отсортированный массив: {orig_list}')
# замеры 1000
print(timeit.timeit("lazy_bubble(orig_list)", setup="from __main__ import lazy_bubble, orig_list", number=1000))
# 53.3634648 мс

finished_bubble(orig_list)
print(f'Отсортированный массив: {orig_list}')
# замеры 1000
print(timeit.timeit("finished_bubble(orig_list)", setup="from __main__ import finished_bubble, orig_list", number=1000))
# 0.0810792 мс
