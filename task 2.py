
"""
Введіть з клавіатури п'ять цілочисельних елементів масиву X.
Виведіть на екран значення коріня і квадратів кожного з елементів масиву.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np
from math import sqrt


answer = '1'
while answer == '1':

    X = np.zeros(5, dtype=int)  # X - масив із 5 заданих цілих чисел

    print("Введіть послідовність з 5 цілих чисел:")
    for i in range(5):  # Введення даних у масив X
        while True:
            try:
                item = int(input())
                break
            except ValueError:
                print("Вводьте правильні дані!")
        X[i] = item

    print("Список коренів чисел заданої послідовності: ", end="")  # Виведення коренів та квадратів елементів масиву X
    for i in range(5):
        print(round(sqrt(X[i]), 3), end="")
        if i != 4:
            print(", ", end="")
    print("\nСписок квадратів чисел заданої послідовності: ", end="")
    for i in range(5):
        print(X[i]**2, end="")
        if i != 4:
            print(", ", end="")

    answer = input("\nВведіть '1' для повторення:")
