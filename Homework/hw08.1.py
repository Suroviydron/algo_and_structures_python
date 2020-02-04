
# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib
import string
import random
from collections import Counter


def string_generator(size, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def counter_solve(s, n):

    obj = Counter()

    for i in range(len(s)):
        if i == 0:
            n = len(s) - 1
        else:
            n = len(s)
        for j in range(n, i, -1):
            print(s[i:j])
            obj[hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()] += 1

    return print(f'Количество различных подстрок в строке {s} равно {len(obj)}')


N = int(input('Введите длину строки: '))
S = string_generator(N)
print(f'Сгенерировалась случайная строка: {S}')
counter_solve(S, N)



