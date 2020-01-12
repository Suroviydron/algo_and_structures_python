__author__ = 'Ablezgov Andrew'

# Задача-2: Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

NUMB_ONE = 5
NUMB_TWO = 6
SHIFT_SIZE = 2

print(f'{NUMB_ONE} = {bin(NUMB_ONE)}')
print(f'{NUMB_TWO} = {bin(NUMB_TWO)}')

print(f'\nС цифрами {NUMB_ONE} и {NUMB_TWO} можно исполнить следующие побитовые операции:\n'
      f'{NUMB_ONE} или {NUMB_TWO} = {bin(NUMB_ONE | NUMB_TWO)} \n'
      f'{NUMB_ONE}  и  {NUMB_TWO} = {bin(NUMB_ONE & NUMB_TWO)} \n'
      f'Сдвиг числа {NUMB_ONE} вправо на {SHIFT_SIZE} знака: {bin(NUMB_ONE >> SHIFT_SIZE)} \n'
      f'Сдвиг числа {NUMB_TWO} влево на {SHIFT_SIZE} знака: {bin(NUMB_TWO << SHIFT_SIZE)}')

