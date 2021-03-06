
"""
Знайти кількість парних елементів одновимірного масиву.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    array, even_num = np.random.randint(1, 100, 20), 0  # array - масив із 20 випадкових цілих чисел від 1 до 100
    # even_num - кількість парних елементів масиву array

    print("Послідовність з 20 випадкових чисел дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")

        if array[i] % 2 == 0:  # Знаходження значень змінної even_num
            even_num += 1
    print(f"\nКількість всіх парних чисел послідовності дорівнює: {even_num}")

    answer = input("Введіть '1' для повторення:")
