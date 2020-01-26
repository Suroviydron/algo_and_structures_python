
# Задача: Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
import memory_profiler
import time

n = int(input('Введите номер запрашиваемого числа: '))


@memory_profiler.profile
def task4_search(num, counter=1, simple_num=2):

    arr = [2]
    while counter != num:
        simple_num += 1
        for i in arr:
            if simple_num % i == 0:
                break
        else:
            arr.append(simple_num)
            counter += 1
    print(f'{num} по счету простое число: {arr[num - 1]}')
    del arr


t1 = time.process_time()
m1 = memory_profiler.memory_usage()

task4_search(n)

t2 = time.process_time()
m2 = memory_profiler.memory_usage()

time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")


@memory_profiler.profile
def eratosthenes(n):

    if n == 1:
        return print('Первое простое число: 2')

    arr_er = [i for i in range(n * 10)]
    arr_er[1] = 0

    for i in range(2, n+1):
        for j in range(i**2, len(arr_er), i):
            if j % i == 0:
                arr_er[j] = 0
    print(f'{n} по счету простое число: {[i for i in arr_er if i != 0][n - 1]}')
    del arr_er


t1 = time.process_time()
m1 = memory_profiler.memory_usage()

eratosthenes(n)

t2 = time.process_time()
m2 = memory_profiler.memory_usage()

time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")

# Результат поиска 5 по счету простого числа:
# 1 способом выполнение заняло 0.03125 сек and 0.30859375 Мб
# C исп. алгоритма РЭ выполнение заняло 0.015625 сек and 0.0 Мб

# Результат поиска 500 по счету простого числа:
# 1 способом выполнение заняло 9.140625 сек and 0.27734375 Мб
# C исп. алгоритма РЭ выполнение заняло 2.125 сек and 0.2578125 Мб

# Результат поиска 1500 по счету простого числа с добавлением функции del:
# 1 способом выполнение заняло 79.109375 сек and 0.2578125 Мб
# C исп. алгоритма РЭ выполнение заняло 7.15625 сек and 0.703125 Мб

# Разница в скорости выполнения алгоритма заметна при поиске высокого по номеру простого числа.
# Скорость при использовании алгоритма "Решето Эратосфена" оптимальнее.
# При этом, из-за генерации большого массива данных процесс занимает больше места в памяти



