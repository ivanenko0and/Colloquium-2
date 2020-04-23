
"""
Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np


answer = '1'
while answer == '1':

    while True:  # Введення значення змінної n, що відповідає за довжину лінійних масивів
        try:
            n = int(input("Введіть довжину двох лінійних масивів:"))
            break
        except ValueError:
            print("Вводьте правильні дані!")

    # array3 - масив, дані якого є добутками відповідних елементів масивів array1 і array2
    array1, array2, array3 = np.zeros(n, dtype=float), np.zeros(n, dtype=float), np.zeros(n, dtype=float)

    print("Введіть коефіцієнти першого масиву:")
    for i in range(n):  # Введення даних у масив array1
        while True:
            try:
                item = float(input())
                break
            except ValueError:
                print("Вводьте правильні дані!")
        array1[i] = item
    print("Введіть коефіцієнти другого масиву:")
    for i in range(n):  # Введення даних у масив array2 та визначення даних масиву array3
        while True:
            try:
                item = float(input())
                break
            except ValueError:
                print("Вводьте правильні дані!")
        array2[i] = item
        array3[i] = round(array1[i] * array2[i], 2)



    print("Перший масив чисел дорівнює:")  # Виведення даних масивів array1, array2 і array3
    for i in range(n):
        print(array1[i], end=" | ")

    print("\nДругий масив чисел дорівнює:")
    for i in range(n):
        print(array2[i], end=" | ")

    print("\nТретій масив, що складається з добутків відповідних елементів двох інших масивів, дорівнює:")
    for i in range(n):
        print(array3[i], end=" | ")

    answer = input("\nВведіть '1' для повторення:")
