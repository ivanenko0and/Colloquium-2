
"""
Підрахувати кількість елементів одновимірного масиву, для яких виконується нерівність i*i<ai<i!

Виконав Іваненко Андрій Вадимович
"""

import numpy as np
from math import factorial

answer = '1'
while answer == '1':

    array, amount = np.random.randint(1, 100, 20), 0  # array - масив із 20 випадкових цілих чисел від 1 до 100
    # amount - кількість елементів масиву array, для яких виконується нерівність i*i<ai<i!

    print("Послідовність з 20 випадкових чисел дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array

        if i * i < array[i] < factorial(i):  # Знаходження значень змінної amount
            amount += 1
            print(f"!{array[i]}!", end="")  # Виділення чисел, для яких виконується нерівність i*i<ai<i!, при виведенні
        else:
            print(array[i], end="")

        if i != 19:
            print(", ", end="")
        else:
            print(".")


    print(f"Кількість чисел послідовності, для яких виконується нерівність i*i < ai < i!, дорівнює: {amount}")

    answer = input("Введіть '1' для повторення:")
