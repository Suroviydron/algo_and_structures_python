
# Задача: В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

COUNTER = 0

for i in range(2, 10):
    for j in range(2, 100):
        if j % i == 0:
            COUNTER += 1
    print(f'{i} - {COUNTER}')
    COUNTER = 0