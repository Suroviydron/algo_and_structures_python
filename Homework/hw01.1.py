__author__ = 'Ablezgov Andrew'

# Задача-1: Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

NUMBER = int(input('Введите трехзначное число: '))

while not NUMBER in range(100, 999):
    NUMBER = int(input('Введите трехзначное число: '))

N_ONE = NUMBER % 10
NUMBER = NUMBER // 10

N_TWO = NUMBER % 10
NUMBER = NUMBER // 10

N_THREE = NUMBER % 10
NUMBER = NUMBER // 10

print(f'Сумма чисел: {N_ONE + N_TWO + N_THREE}\nПроизведение чисел: {N_ONE * N_TWO * N_THREE}')
