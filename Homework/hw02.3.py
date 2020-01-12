__author__ = 'Ablezgov Andrew'

# Задача: Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

def task3(number):

    new_number = 0

    while number >= 1:

        new_number = (new_number * 10) + (number % 10)

        number = number // 10

    return print(f'Обратное число введенному Вами: {new_number}')


task3(3486)