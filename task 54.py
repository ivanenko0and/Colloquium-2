
"""
Введіть масив з 20 елементів і визначте, чи є в ньому елементи з однаковими значеннями.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np


answer = '1'
while answer == '1':

    array, is_repeated = np.zeros(20, dtype=int), False  # array - масив із 20 заданих цілих чисел
    # is_repeated - змінна, яка є істинною, якщо масив array містить в собі однакові елементи

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

        # Перевірка на те, чи належить поточний елемент послідовності, що складається з попередніх елементів
        if array[i] in array[0: i]:
            is_repeated = True

    if is_repeated:
        print("Задана послідовність включає в собі однакові числа.")
    else:
        print("Задана послідовність не включає в собі однакових чисел.")

    answer = input("Введіть '1' для повторення:")
