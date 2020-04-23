
"""
Підрахуйте кількість елементів одновимірного масиву, які збігаються зі своїм номером і при цьому кратні 3.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    array, amount = np.random.randint(0, 30, 30), 0  # array - масив із 30 випадкових цілих чисел від 0 до 30
    # amount - кількість елементів масиву array, які збігаються зі своїм номером і при цьому кратні 3

    print("Послідовність з 30 випадкових чисел дорівнює: ", end="")
    for i in range(30):  # Виведення даних масиву array

        if array[i] == i and array[i] % 3 == 0:  # Знаходження значень змінної amount
            amount += 1
            # Виділення при виведенні чисел, які збігаються зі своїм номером і при цьому кратні 3
            print(f"!{array[i]}!", end="")
        else:
            print(array[i], end="")

        if i != 29:
            print(", ", end="")
        else:
            print(".")

    print(f"Кількість чисел послідовності, які збігаються зі своїм номером і при цьому кратні 3, дорівнює: {amount}")

    answer = input("Введіть '1' для повторення:")