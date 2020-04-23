
"""
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву - 20.
Заповнення масиву здійснити випадковими числами від 100 до 200.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    """ array - масив із 20 випадкових цілих чисел від 100 до 200
    even_num_sum - сума всіх парних елементів масиву array """
    array, even_num_sum = np.random.randint(100, 200, 20), 0

    print("Послідовність з 20 випадкових чисел від 100 до 200 дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")

        if array[i] % 2 == 0:  # Підрахунок значення even_num_sum
            even_num_sum += array[i]
    print(f"\nСума всіх парних чисел послідовності дорівнює: {even_num_sum}")  # Виведення значення even_num_sum

    answer = input("Введіть '1' для повторення:")