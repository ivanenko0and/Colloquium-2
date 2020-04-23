
"""
Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np


answer = '1'
while answer == '1':

    array, positive_num_sum = np.zeros(10, dtype=int), 0  # array - масив із 10 заданих цілих чисел
    # positive_num_sum - сума всіх додатніх елементів масиву array

    print("Введіть послідовність з 10 цілих чисел:")
    for i in range(10):  # Введення даних у масив array
        while True:
            try:
                item = int(input())
                break
            except ValueError:
                print("Вводьте правильні дані!")
        array[i] = item

    print("Задана послідовність чисел дорівнює: ", end="")
    for i in range(10):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 9:
            print(", ", end="")
        else:
            print(".")

        if array[i] > 0:  # Знаходження суми всіх додатніх елементів масиву array
            positive_num_sum += array[i]

    print(f"Сума всіх додатніх чисел послідовності дорівнює: {positive_num_sum}")  # Виведення значення positive_num_sum

    answer = input("Введіть '1' для повторення:")
