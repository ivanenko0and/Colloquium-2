
"""
Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних чисел в ньому.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np


answer = '1'
while answer == '1':

    array, numbers = np.zeros(10, dtype=int), []  # array - масив із 10 заданих цілих чисел
    # numbers - список з всіх різних чисел масиву array

    print("Введіть послідовність з 10 цілих чисел:")
    for i in range(10):  # Введення даних у масив array
        while True:
            try:
                item = int(input())
                break
            except ValueError:
                print("Вводьте правильні дані!")
        array[i] = item

        if item not in numbers:  # Заповнення списку numbers
            numbers.append(item)

    print("Задана послідовність чисел дорівнює: ", end="")
    for i in range(10):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 9:
            print(", ", end="")
        else:
            print(".")

    print(f"Кількість різних чисел в заданій послідовності дорівнює: {len(numbers)}.")

    answer = input("Введіть '1' для повторення:")
