
# Задача: Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

from timeit import Timer

# Сложность данного массива: O(n) - линейная


def task_1version(arr):

    arr2 = []

    for i, j in enumerate(arr):
        if j % 2 == 0:
            arr2.append(i)

    return print(f'Список индексов четных элементов заданного массива: {arr2}')


def task_2version(arr):

    return print(f'Список индексов четных элементов заданного массива: {[i for i in range(len(arr)) if (arr[i] % 2 == 0)]}')


t1 = Timer("task_1version([8, 3, 15, 6, 4, 2])", "from __main__ import task_1version")
print("task 1 version ", t1.timeit(number=1), "milliseconds")

t2 = Timer("task_2version([8, 3, 15, 6, 4, 2])", "from __main__ import task_2version")
print("task 2 version ", t2.timeit(number=1), "milliseconds")