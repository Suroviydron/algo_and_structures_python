__author__ = 'Ablezgov Andrew'

# Задача: Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

INPUT_NUMB = int(input("Сколько будет чисел? "))
MAX_NUMB = 0
MAX_SUMM = 0

while INPUT_NUMB > 0:

    NUMBER = int(input('Введите число: '))
    SUMM_NUMB = 0
    COPY = NUMBER

    while NUMBER >= 1:

        SUMM_NUMB = SUMM_NUMB + NUMBER % 10
        NUMBER = NUMBER // 10

    if SUMM_NUMB > MAX_SUMM:
        MAX_SUMM = SUMM_NUMB
        MAX_NUMB = COPY

    INPUT_NUMB -= 1

print(f'Наибольшее число по сумме цифр: {MAX_NUMB}. Сумма цифр данного числа: {MAX_SUMM}')