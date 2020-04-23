
"""
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np


answer = '1'
while answer == '1':

    """ array - масив із 20 заданих цілих чисел.
    nonzero_num_product - добуток ненульових елементів масиву array.

    Для проведення підрахунку добутку початкове значення nonzero_num_product має дорівнювати одиниці.
    Якщо масив не містить в собі ненульових чисел, то добуток залише значення одиниці, якій добуток не має дорівнювати. 
    Для перевірки, того, чи відбулось множення, використовується змінна is_multiplied. """
    array, nonzero_num_product, is_multiplied = np.zeros(20, dtype=int), 1, False

    print("Введіть послідовність з 20 цілих чисел:")
    for i in range(20):  # Введення даних у масив array
        while True:
            try:
                item = int(input())
                break
            except ValueError:
                print("Вводьте правильні дані!")
        array[i] = item

    print("Задана послідовність чисел дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")
        else:
            print(".")

        if array[i] != 0:  # Підрахунок значення nonzero_num_product
            nonzero_num_product = round(nonzero_num_product * array[i], 2)
            is_multiplied = True  # Якщо відбулось хоча б одне множення значення is_multiplied стає істинним

    if is_multiplied:  # Виведення відповідного тексту в залежності від значення is_multiplied
        print(f"Добуток всіх ненульових чисел цієї послідовності дорівнює: {nonzero_num_product}.")
    else:
        print("Ця послідовність чисел містить в собі тільки нулі.")

    answer = input("Введіть '1' для повторення:")
