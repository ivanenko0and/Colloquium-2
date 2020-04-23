
"""
Напишіть програму аналізу значень температури хворого за добу: визначте мінімальне і максимальне значення,
середнє арифметичне. Заміри температури виробляються шість раз на добу і результати вводяться з клавіатури у масив T.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    """ T - масив, що містить результати шістьох вимірювань температури хворого за добу, які вводяться користувачем.
    min_temp - мінімальне значення температури у масиві T.
    max_temp - максимальне значення температури у масиві T.
    arithmetic_mean - середнє арифметичне значень температури."""
    T, min_temp, max_temp, arithmetic_mean = np.zeros(6), 100, 0, 0

    print("Введіть результати 6 вимірювань температури хворого:")
    for i in range(6):  # Введення даних у масив T
        while True:
            try:
                item = float(input())
                break
            except ValueError:
                print("Вводьте правильні дані!")
        T[i] = item

        if item < min_temp:  # Знаходження значень змінних min_temp, max_temp і arithmetic_mean
            min_temp = item
        if item > max_temp:
            max_temp = item
        arithmetic_mean += item
    arithmetic_mean = round(arithmetic_mean / 6, 1)

    print("Список результатів 6 вимірювань температури хворого за добу дорівнює: ", end="")
    for i in range(6):  # Виведення даних масиву T та значень змінних min_temp, max_temp і arithmetic_mean
        print(T[i], "°C", end="")
        if i != 5:
            print(", ", end="")
    print(f"\nМінімальне значення температури дорівнює: {min_temp}."
          f"\nМаксимальне значення температури дорівнює: {max_temp}."
          f"\nСереднє арифметичне значень температури дорівнює: {arithmetic_mean}.")

    answer = input("Введіть '1' для повторення:")
