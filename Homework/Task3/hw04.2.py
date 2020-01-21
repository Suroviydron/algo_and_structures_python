
# Задача: Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

from timeit import Timer
import cProfile

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

    task4_search(n, counter, simple_num)


n = int(input('Введите i число: '))

t1 = Timer("task4_search(n)", "from __main__ import task4_search", globals={"n": n})
print("Поиск простого числа занял ", t1.timeit(number=1), "мс")


cProfile.run('task4_search(n)')




