__author__ = 'Ablezgov Andrew'

# Задача: Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

NUMBER = int(input("Сколько будет чисел? "))
TARGET = int(input("Какую цифру считать? "))
COUNTER = 0

for i in range(1, NUMBER + 1):
    ARRAY = int(input("Число " + str(i) + ": "))
    while ARRAY > 0:
        if ARRAY % 10 == TARGET:
            COUNTER += 1
        ARRAY = ARRAY // 10

print(f'Было введено {COUNTER} запрашиваемых цифр')


