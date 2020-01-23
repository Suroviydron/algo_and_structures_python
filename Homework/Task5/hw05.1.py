
# Задача: Пользователь вводит данные о количестве предприятий, их наименования и прибыль за
# 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю
# прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
from builtins import sum
from collections import namedtuple
from random import randint

n = int(input('Введите количество предприятий: '))

PROFIT = []
INFO = []
MAX_PROFIT = []
MIN_PROFIT = []

POINT = namedtuple('Companies_Info', 'id name profit_1q profit_2q profit_3q profit_4q')

for i in range(n):

    COMPANY = POINT(i, input('Введите название фирмы: '), randint(0, 10000),
                    randint(0, 10000), randint(0, 10000), randint(0, 10000))

    INFO.append(COMPANY)
    PROFIT.append(COMPANY.profit_1q + COMPANY.profit_2q + COMPANY.profit_3q + COMPANY.profit_4q)
    print(f'Приыбль компании {COMPANY.name} составила {PROFIT[i]}')

PROFIT_AVG = sum(PROFIT) / n

for idx, j in enumerate(PROFIT):
    if j > PROFIT_AVG:
        MAX_PROFIT.append(INFO[idx].name)
    else:
        MIN_PROFIT.append(INFO[idx].name)

print(f'Средня прибыль компаний в текущем году: {PROFIT_AVG}.\n'
      f'Компании(я) с прибылью выше среднего:', end=" ")
for i in MAX_PROFIT:
    print(i, end=",")
print('\nниже среднего: ', end=" ")
for i in MIN_PROFIT:
    print(i, end=" ")

