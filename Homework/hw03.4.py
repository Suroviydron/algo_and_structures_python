__author__ = 'Ablezgov Andrew'

# Задача: Определить, какое число в массиве встречается чаще всего.

LIST = [1, 2, 4, 6, 8, 1, 5, 9, 4, 4, 1, 5, 5]
number = []

def list_check(array):
    repeat_numb = 0

    for i in range(len(array) - 1):

        counter = 1

        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                counter += 1

        if counter > repeat_numb and counter >= 2:
            number = []
            repeat_numb = counter
            number.append(array[i])
        elif counter == repeat_numb and counter >= 2:
            repeat_numb = counter
            number.append(array[i])

    if repeat_numb >= 2 and len(number) > 1:
        print(f'В сформировавшемся массиве {repeat_numb} повторений чисел:', end=' ')
        for k in number:
            print(k, end=' ')
        print('')
        return
    elif repeat_numb >= 2 and len(number) == 1:
        return print(f'В сформировавшемся массиве {repeat_numb} повторений числа: {number[0]}')
    else:
        return print('В массиве нет повторяющихся чисел')


list_check([1, 2, 4, 6, 8, 1, 5, 9, 4, 4, 1, 5, 5])
list_check([1, 2, 4, 6, 8, 1, 5, 9, 4, 1, 1, 5])
list_check([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
