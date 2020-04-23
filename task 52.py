
"""
Знайти найбільший елемент з елементів одновимірного масиву, що мають парний номер. Визначити, чи є він єдиним.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    """ array - масив із 20 випадкових цілих чисел від 1 до 100.
    max_even_num - максимальний парний елемент масиву array.
    is_repeated - змінна, яка є істинною, якщо максимальний парний елемент масиву array повторюється. """
    array, max_even_num, is_repeated = np.random.randint(1, 100, 20), 0, False


    print("Послідовність з 20 випадкових чисел дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")
        else:
            print(".")

        # Якщо максимальний парний елемент масиву array повторюється, змінна is_repeated приймає значення істинності
        if max_even_num == array[i]:
            is_repeated = True

        if array[i] % 2 == 0 and array[i] > max_even_num:  # Знаходження значень змінної max_even_num
            max_even_num = array[i]
            is_repeated = False  # Якщо значення max_even_num змінюється, то is_repeated приймає значення хибності

    print(f"Максимальний парний елемент послідовності випадкових чисел дорівнює: {max_even_num}")

    if is_repeated:
        print("Максимальний парний елемент послідовності випадкових чисел неповторюється.")
    else:
        print("Максимальний парний елемент послідовності випадкових чисел повторюється.")

    answer = input("Введіть '1' для повторення:")
