
# Задача: Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
import timeit

arr = [2]


def task4_search(num, counter=1, simple_num=2):

    if counter == num:
        return print(f'{num} по счету простое число: {arr[num-1]}')

    simple_num += 1

    for i in arr:
        if simple_num % i == 0:
            break
    else:
        arr.append(simple_num)
        counter += 1

    task4_search(num, counter, simple_num)


def eratosthenes(n):

    if n == 1:
        return print('Первое простое число: 2')

    arr_er = [i for i in range(n**2)]
    arr_er[1] = 0

    for i in range(2, n+1):
        for j in range(i**2, len(arr_er), i):
            if j % i == 0:
                arr_er[j] = 0

    return print(f'{n} по счету простое число: {[i for i in arr_er if i != 0][n-1]}')


n = int(input('Введите номер запрашиваемого числа: '))

print(timeit.timeit("task4_search(n)", setup="from __main__ import task4_search, n", number=1))

print(timeit.timeit("eratosthenes(n)", setup="from __main__ import eratosthenes, n", number=1))

# Результат поиска 5 по счету простого числа:
# Время расчета задачи 1 способом:  3.59 мс
# Время расчета задачи с исп. алгоритма РЭ:  2.96 мс

# Результат поиска 1000 по счету простого числа:
# Время расчета задачи 1 способом:  6.55 мс
# Время расчета задачи 2 способом:  0.32 мс

# Время, затрачиваемое на обработку задачи, меняется в зависимости от величины заданного простого числа.
# Учитывая изложенное, в случае необходимости поиска больших простых чисел рассчет задачи
# оптимальнее производить, используя алгоритм "Решето Эратосфена".



