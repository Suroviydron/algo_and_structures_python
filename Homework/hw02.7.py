__author__ = 'Ablezgov Andrew'

# Задача: Напишите программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


def task7(n, summ=3, a=2):

    if n == a:
        if summ == (a * (a + 1) / 2):
            return print('Выполняется условие')
        else:
            return print('Условие не выполняется')
    else:
        a += 1
        summ = summ + a
        task7(n, summ, a)


NUMBER = int(input('Введите длину множества: '))
task7(NUMBER)