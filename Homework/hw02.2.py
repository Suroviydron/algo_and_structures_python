__author__ = 'Ablezgov Andrew'

# Задача: Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def task2(number):

    even_numb = 0
    odd_numb = 0

    while number >= 1:

        if (number % 10) % 2 == 0:
            even_numb += 1
        else:
            odd_numb += 1

        number = number // 10

    return print(f'В указанном числе {even_numb} четных цифр и {odd_numb} нечетных нечетных')

task2(34560)