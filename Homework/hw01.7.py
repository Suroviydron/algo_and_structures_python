__author__ = 'Ablezgov Andrew'

# Задача-7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он
# разносторонним, равнобедренным или равносторонним

print('Введите длины сторон предполагаемого треугольника.')
SIDE_ONE = int(input('Сторона a = '))
SIDE_TWO = int(input('Сторона b = '))
SIDE_THREE = int(input('Сторона c = '))

if SIDE_ONE + SIDE_TWO <= SIDE_THREE or SIDE_ONE + SIDE_THREE <= SIDE_TWO or SIDE_TWO + SIDE_THREE <= SIDE_ONE:
    print('Треугольник не существует')
elif SIDE_ONE == SIDE_TWO == SIDE_THREE:
    print("Представленный треугольник - равносторонний")
elif SIDE_ONE != SIDE_TWO and SIDE_ONE != SIDE_THREE and SIDE_TWO != SIDE_THREE:
    print("Представленный треугольник - разносторонний")
else:
    print("Представленный треугольник - равнобедренный")

