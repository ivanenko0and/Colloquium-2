"""
Обчислити середнє арифметичне значення тих елементів одновимірного масиву, які потрапляють в інтервал від -2 до 10.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    """ array - масив із 20 випадкових цілих чисел від -50 до 50.
    arithmetic_mean - середнє арифметичне значення елементів масиву array, які потрапляють в інтервал від -2 до 10.
    amount - кількість елементів, які потрапляють в інтервал від -2 до 10. """
    array, arithmetic_mean, amount = np.random.randint(-50, 50, 20), 0, 0

    print("Послідовність з 20 випадкових чисел дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")
        else:
            print(".")

        if -2 < array[i] < 10:  # Знаходження значення arithmetic_mean
            arithmetic_mean += array[i]
            amount += 1
    arithmetic_mean = round(arithmetic_mean / amount, 2)

    print(f"Середнє арифметичне значення чисел послідовності в інтервалі від -2 до 10 дорівнює: {arithmetic_mean}")

    answer = input("Введіть '1' для повторення:")
