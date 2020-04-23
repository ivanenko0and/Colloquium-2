
"""
Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому повторюється найчастіше число.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np


answer = '1'
while answer == '1':

    array, numbers = np.zeros(10, dtype=int), {}  # array - масив із 10 заданих цілих чисел
    # numbers - словник з всіх різних чисел масиву array разом з кількістю їх повторів
    max_frequency, max_frequency_num = 0, 0  # max_frequency - максимальна кількість повторів серед всіх чисел
    # max_frequency_num - число з найбільшою кількістю повторів у масиві array

    print("Введіть послідовність з 10 цілих чисел:")
    for i in range(10):  # Введення даних у масив array
        while True:
            try:
                item = int(input())
                break
            except ValueError:
                print("Вводьте правильні дані!")
        array[i] = item

        if item not in numbers:  # Заповнення словника numbers
            numbers[item] = 1
        else:
            numbers[item] += 1

    print("Задана послідовність чисел дорівнює: ", end="")
    for i in range(10):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 9:
            print(", ", end="")
        else:
            print(".")

    for i in numbers:  # Знаходження числа з найбільшою кількістю повторів у масиві array
        if max_frequency < numbers[i]:
            max_frequency = numbers[i]
            max_frequency_num = i

    print(f"Число заданої послідовності, яке найчастіше повторюється є число {max_frequency_num} "
          f"з повторюваністю {max_frequency}.")

    answer = input("Введіть '1' для повторення:")
