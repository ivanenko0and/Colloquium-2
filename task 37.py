
"""
Розсортуйте заданий лінійний масив по зростанню.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np
    

answer = '1'
while answer == '1':

    array = np.zeros(10, dtype=int)  # array - масив із 10 заданих цілих чисел

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

    # Алгоритм сортування вставками
    for i in range(1, 10):
        insert_item = array[i]  # insert_item - поточний елемент для порівняння
        j = i - 1
        """ Якщо існує послідовність елементів, що розміщені підряд за insert_item і більші за нього, то ця 
        послідовність зміщується вперед на один елемент """
        while j >= 0 and array[j] > insert_item:
            array[j + 1] = array[j]
            j -= 1
        """ insert_item переміщується на місце перед послідовністю більших за нього чисел та після елемента, 
        що менше за нього """
        array[j + 1] = insert_item

    print("Відсортована послідовність дорівнює: ", end="")
    for i in range(10):  # Виведення даних відсортованого масиву array
        print(array[i], end="")
        if i != 9:
            print(", ", end="")
        else:
            print(".")

    answer = input("Введіть '1' для повторення:")
