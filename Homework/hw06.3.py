# Задача: Написать программу, которая генерирует отсортированный массив из 10000 чисел
# в указанных пользователем границах (0, 1000):

import memory_profiler
import time
from random import random, randint


def first_try(left, right):
    arr = []
    for i in range(10000):
        number = int(random() * (right - left + 1) + left)
        arr.append(number)
    for i in range(9999):
        for j in range(i + 1, 10000):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return print(arr)


def second_try(left, right):
    second_arr = [randint(left, right) for i in range(10000)]
    second_arr.sort()
    print(second_arr)
    del left, right, second_arr
    return


LEFT_BOARD = int(input('Введите минимальное значение: '))
RIGHT_BOARD = int(input('Введите максимальное значение: '))

t1 = time.process_time()
m1 = memory_profiler.memory_usage()
first_try(LEFT_BOARD, RIGHT_BOARD)
t2 = time.process_time()
m2 = memory_profiler.memory_usage()

time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")

t1 = time.process_time()
m1 = memory_profiler.memory_usage()
second_try(LEFT_BOARD, RIGHT_BOARD)
t2 = time.process_time()
m2 = memory_profiler.memory_usage()

time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")

# Первый вариант использует алгоритмы, пройденные в 1 Задании. Он занимает больше памяти и времени на выполнение
# Второй алгоритм оптимальнее и предпочтительней к использованию, так как выполняется быстрее и занимает меньше памяти.

