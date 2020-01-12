__author__ = 'Ablezgov Andrew'

# Задача-9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

NUMB_ONE = int(input('Введите первое число: '))
NUMB_TWO = int(input('Введите второе число: '))
NUMB_THREE = int(input('Введите третье число: '))

if (NUMB_ONE > NUMB_TWO and NUMB_ONE < NUMB_THREE) or (NUMB_ONE > NUMB_THREE and NUMB_ONE < NUMB_TWO):
    print(f'{NUMB_ONE} является средним числом из трех введенных Вами')
elif (NUMB_TWO > NUMB_ONE and NUMB_TWO < NUMB_THREE) or (NUMB_TWO > NUMB_THREE and NUMB_TWO < NUMB_ONE):
    print(f'{NUMB_TWO} является средним числом из трех введенных Вами')
else:
    print(f'{NUMB_THREE} является средним числом из трех введенных Вами')