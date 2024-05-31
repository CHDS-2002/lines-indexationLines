# os - библиотека для работы с консолью
# random - библиотека для работы со случайными данными
import os
import random

# Зададим цвет шрифта консоли
os.system('COLOR B')

LEFT = 1040  # LEFT - левая граница
RIGHT = 1103  # RIGHT - правая граница
RANGE = (RIGHT - LEFT) // 5  # RANGE - диапозон значений

literals = [chr(random.randint(LEFT, RIGHT)) for _ in range(RANGE)]
# literals - сгенерированные случайные символы
example = ''.join(literals)
# example - строка случайных символов

# Сделаем анализ строки
first = example[0]  # first - первый символ
last = example[-1]  # last - последний символ
second_half = example[len(example) // 2:]  # second_half - вторая половина строки
reverse_line = example[::-1]  # reverse_line - перевёрнутая строка
odd_line = example[1::2]  # odd_line - строка с чётными символами

print('\nАНАЛИЗ СТРОКИ\n')
print('Строка: ', example, '.', sep='')
print('Первый символ: ', first, '.', sep='')
print('Последний символ: ', last, '.', sep='')
print('Вторая половина строки: ', second_half, '.', sep='')
print('Перевёрнутая строка: ', reverse_line, '.', sep='')
print('Строка с чётными символами: ', odd_line, '.\n', sep='')

try:
    os.system('PAUSE')  # Завершаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
