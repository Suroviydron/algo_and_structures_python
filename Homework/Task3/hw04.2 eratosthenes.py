
# Задача: Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
from timeit import Timer


def eratosthenes(n):

    if n == 1:
        return print('Первое простое число: 2')

    arr = [i for i in range(n**2)]
    arr[1] = 0

    for i in range(2, n+1):
        for j in range(i**2, len(arr), i):
            if j % i == 0:
                arr[j] = 0

    simple_num = [i for i in arr if i != 0]
    return print(f'{n} простое число: {simple_num[n-1]}')


num = int(input('Введите i число: '))

t1 = Timer("eratosthenes(num)", "from __main__ import eratosthenes", globals={"num": num})
print("Поиск простого числа занял ", t1.timeit(number=1), "мс")






