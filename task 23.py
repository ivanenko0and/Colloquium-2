
"""
Знайти суму всіх елементів масиву цілих чисел, які менше середнього арифметичного елементів масиву.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 150 до 300.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    """ array - масив із 20 випадкових цілих чисел від 150 до 300.
    num_sum - суму всіх елементів масиву array, які менше середнього арифметичного елементів масиву.
    arithmetic_mean - середнє арифметичне елементів масиву array. """
    array, num_sum, arithmetic_mean = np.random.randint(150, 300, 20), 0, 0

    print("Послідовність з 20 випадкових чисел від 150 до 300 дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")

        arithmetic_mean += array[i]  # Знаходження значення середнього арифметичного масиву
    arithmetic_mean = round(arithmetic_mean / 20, 2)
    print(f"\nСереднє арифметичне послідовності чисел дорівнює: {arithmetic_mean}")

    for i in array:  # Знаходження значення num_sum
        if i < arithmetic_mean:
            num_sum += i

    print(f"Сума всіх чисел послідовності, менших середнього арифметичного послідовності, дорівнює: {num_sum}")

    answer = input("Введіть '1' для повторення:")