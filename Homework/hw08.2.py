
# Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter, deque

binary_tabl = dict()


def haf_tree(s):

    obj = Counter(s)
    sort_obj = deque(sorted(obj.items(), key=lambda pair: pair[1]))
    print(f'Отсортированный по частоте повторения счетчик: {sort_obj}')

    count = 1
    if len(sort_obj) != 1:

        while len(sort_obj) > 1:
            print(f'\nПроход № {count}')
            count += 1

            weight = sort_obj[0][1] + sort_obj[1][1]
            arr = {0: sort_obj.popleft()[0], 1: sort_obj.popleft()[0]}
            print(f'Два выбранных элемента {arr}, их частота: {weight}')

            for idx, j in enumerate(sort_obj):
                if weight > j[1]:
                    continue
                else:
                    sort_obj.insert(idx, (arr, weight))
                    print(f'Получившийся массив со вставкой: {sort_obj}')
                    break
            else:
                sort_obj.append((arr, weight))

    else:
        weight = sort_obj[0][1]
        arr = {0: sort_obj.popleft()[0], 1: None}
        sort_obj.append((arr, weight))

    return sort_obj[0][0]


def haf_cd(tree, path=''):

    if not isinstance(tree, dict):
        binary_tabl[tree] = path
    else:
        haf_cd(tree[0], path=f'{path}0')
        haf_cd(tree[1], path=f'{path}1')


S = "beep boop beer!"
haf_cd(haf_tree(S))

print('Закодированная строка: ')
for i in S:
    print(binary_tabl[i], end=' ')



