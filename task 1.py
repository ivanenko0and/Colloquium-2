
"""
Введіть з клавіатури в масив п'ять цілочисельних значень.
Виведіть їх в один рядок через кому. Отримайте для масиву середнє арифметичне.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np


answer = '1'
while answer == '1':

    array, arithmetic_mean = np.zeros(5, dtype=int), 0  # array - масив із 5 заданих цілих чисел
    # arithmetic_mean - змінна, що містить середнє арифметичне чисел масиву array

    print("Введіть послідовність з 5 цілих чисел:")
    for i in range(5):  # Введення даних у масив array
        while True:
            try:
                item = int(input())
                break
            except ValueError:
                print("Вводьте правильні дані!")
        array[i] = item

    print("Задана послідовність чисел дорівнює: ", end="")
    for i in range(5):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 4:
            print(", ", end="")

        arithmetic_mean += array[i]  # Знаходження суми чисел масиву array

    arithmetic_mean //= len(array)  # Знаходження середнього арифметичного чисел масиву array
    print(f"\nСереднє арифметичне цих чисел дорівнює: {arithmetic_mean}")  # Виведення значення arithmetic_mean

    answer = input("Введіть '1' для повторення:")
