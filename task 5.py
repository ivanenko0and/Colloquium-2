
"""
Створіть масив А [1..7] за допомогою генератора випадкових чисел і виведіть його на екран.
Збільште всі його елементи в 2 рази.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    array = np.random.randint(-20, 20, 7)  # array - масив із 7 випадкових цілих чисел від -20 до 20

    print("Послідовність з 7 випадкових чисел дорівнює: ", end="")
    for i in range(7):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 6:
            print(", ", end="")
    print("\nПослідовність з випадкових чисел, які були збільшені у два рази, дорівнює: ", end="")
    for i in range(7):  # Виведення збільшених у два рази даних масиву array
        array[i] *= 2
        print(array[i], end="")
        if i != 6:
            print(", ", end="")

    answer = input("\nВведіть '1' для повторення:")
