
# Задача: Пользователь вводит данные о количестве предприятий, их наименования и прибыль за
# 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю
# прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
from builtins import sum
from collections import namedtuple
from random import randint
from memory_profiler import profile


@profile
def task(n):

    profit = []
    info = []
    max_profit = []
    min_profit = []

    POINT = namedtuple('Companies_Info', 'id INN profit_1q profit_2q profit_3q profit_4q')

    for i in range(n):

        company = POINT(i, randint(100000000, 999999999), randint(10000, 1000000),
                        randint(10000, 1000000), randint(10000, 1000000), randint(10000, 1000000))

        info.append(company)
        profit.append(company.profit_1q + company.profit_2q + company.profit_3q + company.profit_4q)
        print(f'Приыбль компании {company.INN} составила {profit[i]}')

    profit_avg = sum(profit) / n

    for idx, j in enumerate(profit):
        if j > profit_avg:
            max_profit.append(info[idx].INN)
        else:
            min_profit.append(info[idx].INN)

    print(f'Средня прибыль компаний в текущем году: {profit_avg}.\n'
          f'Компании(я) с прибылью выше среднего:', end=" ")
    del profit, info, profit_avg, company, n
    for i in max_profit:
        print(i, end=",")
    print('\nниже среднего: ', end=" ")
    for i in min_profit:
        print(i, end=" ")
    del max_profit, min_profit


number = int(input('Введите количество предприятий: '))
task(number)

"""
При проведении анализа пришел к выводу, что для небольшого числа предприятий (< 1000) объем занимаемой памяти
практички не играет роли. Соответственно profile и del не имеют важности.

Вывод данных о прибыли для 10000 компаний:
Line #    Mem usage    Increment   Line Contents
================================================
    12     15.6 MiB     15.6 MiB   @profile
    13                             def task(n):
    14                             
    15     15.6 MiB      0.0 MiB       profit = []
    16     15.6 MiB      0.0 MiB       info = []
    17     15.6 MiB      0.0 MiB       max_profit = []
    18     15.6 MiB      0.0 MiB       min_profit = []
    19                             
    20     15.7 MiB      0.0 MiB       POINT = namedtuple('Companies_Info', 'id INN profit_1q profit_2q profit_3q profit_4q')
    21                             
    22     49.5 MiB      0.0 MiB       for i in range(n):
    23                             
    24     49.5 MiB      0.1 MiB           company = POINT(i, randint(100000000, 999999999), randint(10000, 1000000),
    25     49.5 MiB      0.1 MiB                           randint(10000, 1000000), randint(10000, 1000000), randint(10000, 1000000))
    26                             
    27     49.5 MiB      0.5 MiB           info.append(company)
    28     49.5 MiB      0.7 MiB           profit.append(company.profit_1q + company.profit_2q + company.profit_3q + company.profit_4q)
    29     49.5 MiB      0.0 MiB           print(f'Приыбль компании {company.INN} составила {profit[i]}')
    30                             
    31     49.5 MiB      0.0 MiB       profit_avg = sum(profit) / n
    32                             
    33     50.0 MiB      0.0 MiB       for idx, j in enumerate(profit):
    34     50.0 MiB      0.0 MiB           if j > profit_avg:
    35     50.0 MiB      0.1 MiB               max_profit.append(info[idx].INN)
    36                                     else:
    37     50.0 MiB      0.1 MiB               min_profit.append(info[idx].INN)
    38                             
    39     50.0 MiB      0.0 MiB       print(f'Средня прибыль компаний в текущем году: {profit_avg}.\n'
    40     50.0 MiB      0.0 MiB             f'Компании(я) с прибылью выше среднего:', end=" ")
    41     47.5 MiB      0.0 MiB       del profit, info, profit_avg, company, n
    42     47.5 MiB      0.0 MiB       for i in max_profit:
    43     47.5 MiB      0.0 MiB           print(i, end=",")
    44     47.5 MiB      0.0 MiB       print('\nниже среднего: ', end=" ")
    45     47.5 MiB      0.0 MiB       for i in min_profit:
    46     47.5 MiB      0.0 MiB           print(i, end=" ")
    47     16.6 MiB      0.0 MiB       del max_profit, min_profit
    
"""
