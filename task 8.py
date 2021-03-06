
"""
Створіть цілочисельний масив А [1..15] за допомогою генератора випадкових чисел з елементами від -15 до 30
і виведіть його на екран. Визначте найбільший елемент масиву і його індекс.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    array, max_num_index = np.random.randint(-15, 30, 15), 0  # array - масив із 15 випадкових цілих чисел від -15 до 30
    # max_num_index - індекс найбільшого елемента масиву array

    print("Послідовність з 15 випадкових чисел від -15 до 30 дорівнює: ", end="")
    for i in range(15):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 14:
            print(", ", end="")
        if array[i] > array[max_num_index]:  # Знаходження найбільшого елемента масиву array
            max_num_index = i
    # Виведення значення та індексу найбільшого елемента масиву array
    print(f"\nНайбільше з цих чисел дорівнює {array[max_num_index]} та має індекс {max_num_index}.")

    answer = input("\nВведіть '1' для повторення:")
