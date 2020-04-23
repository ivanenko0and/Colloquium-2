"""
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    """ array - масив із 20 випадкових цілих чисел від 1 до 100.
    min_num - мінімальний елемент масиву array.
    arithmetic_mean - середнє арифметичне значення елементів масиву array, які розташовані за першим по порядку 
    мінімальним елементом масиву.
    index - індекс першого по порядку мінімального елементу масиву/кількість елементів до першого входження
    мінімального елементу масиву. """
    array, min_num, arithmetic_mean, index = np.random.randint(1, 100, 20), 100, 0, 0

    print("Послідовність з 20 випадкових чисел дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")
        else:
            print(".")

        if array[i] < min_num:  # Знаходження мінімального елементу масиву array
            min_num = array[i]
            index = i

    for i in range(20):  # Знаходження значення arithmetic_mean
        # Коли зустрічається перше входження числа min_num підрахунок arithmetic_mean припиняється
        if array[i] == min_num:
            break
        arithmetic_mean += array[i]
    arithmetic_mean = round(arithmetic_mean / index, 2)

    # Виведення значення arithmetic_mean
    print("Середнє арифметичне значення чисел послідовності, до першого входження "
          f"мінімального числа масиву ({min_num}), дорівнює: {arithmetic_mean}")

    answer = input("Введіть '1' для повторення:")
