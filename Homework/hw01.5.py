__author__ = 'Ablezgov Andrew'

# Задача-5: Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

LETTER_ONE = ord(input('Введите первую букву: ')) - 96
LETTER_TWO = ord(input('Введите вторую букву: ')) - 96

print(f'Вы ввели {LETTER_ONE} букву алфавита и {LETTER_TWO} букву алфавита.\n')

if LETTER_TWO == LETTER_ONE:
    print('Вы ввели одинаковые буквы')

elif LETTER_TWO > LETTER_ONE:
    DIFFERENCE = LETTER_TWO - LETTER_ONE
    if DIFFERENCE == 1:
        print('Вы ввели соседние буквы')
    else:
        print(f'Между ними {DIFFERENCE - 1} букв')
else:
    DIFFERENCE = 26 - LETTER_ONE + LETTER_TWO - 1
    if DIFFERENCE == 0:
        print('Вы ввели соседние буквы')
    else:
        print(f'Между ними {DIFFERENCE} букв')
