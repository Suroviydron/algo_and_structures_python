
# Задача: Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
from collections import defaultdict


def task_sum(first, second):
    num_sum = hex(first + second)
    arr = [i.upper() for i in num_sum]
    return arr[2:]


def task_product(first, second):
    num_prod = hex(first * second)
    arr = [i.upper() for i in num_prod]
    return arr[2:]


def convert_dict(arr):
    c = 0
    for idx, j in enumerate(arr, start=1):
        c = c + int(j, 16) * 16**(len(arr) - idx)
    return c


DEF_DICT = defaultdict(list)
DEF_DICT['Первое число:'] = [i for i in input('Введите число: ')]
DEF_DICT['Второе число:'] = [i for i in input('Введите число: ')]

FIRST = convert_dict(DEF_DICT['Первое число:'])
SECOND = convert_dict(DEF_DICT['Второе число:'])

print(f'{task_sum(FIRST, SECOND)}')
print(f'{task_product(FIRST, SECOND)}')















