"""
В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи масиву так, щоб спочатку розташовувалися
всі нулі, потім все одиниці, а потім всі п'ятірки. Додаткового масиву не заводити.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np


answer = '1'
while answer == '1':

    while True:  # Введення значення змінної n, яка буде довжиною лінійного масиву X
        try:
            n = int(input("Введіть довжину послідовності чисел:"))
            if n > 0:
                break
            else:
                print("Вводьте правильні дані!")
        except ValueError:
            print("Вводьте правильні дані!")

    X = np.random.choice([0, 1, 5], n)  # X - масив із n випадково вибраних чисел з цифр 0, 1 і 5

    print(f"Послідовність з {n} випадково вибраних чисел з цифр 0, 1 і 5 дорівнює: ", end="")
    for i in range(n):  # Виведення даних масиву X
        print(X[i], end="")
        if i != n - 1:
            print(", ", end="")
        else:
            print(".")

    # Алгоритм сортування вставками
    for i in range(1, n):
        insert_item = X[i]  # insert_item - поточний елемент для порівняння
        j = i - 1
        """ Якщо існує послідовність елементів, що розміщені підряд за insert_item і більші за нього, то ця 
        послідовність зміщується вперед на один елемент """
        while j >= 0 and X[j] > insert_item:
            X[j + 1] = X[j]
            j -= 1
        """ insert_item переміщується на місце перед послідовністю більших за нього чисел та після елемента, 
        що менше за нього """
        X[j + 1] = insert_item

    print("Відсортована послідовність з випадкових чисел дорівнює: ", end="")
    for i in range(n):  # Виведення даних відсортованого масиву X
        print(X[i], end="")
        if i != n - 1:
            print(", ", end="")
        else:
            print(".")

    answer = input("Введіть '1' для повторення:")
