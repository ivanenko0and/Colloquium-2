
"""
Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np
from math import sqrt


answer = '1'
while answer == '1':

    """ array - масив із 9 значень довжин опор.
    Оскільки опори розташовані на відстані R / 5 один від одного, то ці опори разом зі стінками даху розділяють 
    діаметр півкола на (2 * R) / (R / 5) = (10 * R) / R = 10 ділянок. Так як опори розташовані між цими ділянками, то 
    дах завжди будуть підтримувати 10 - 1 = 9 опор, незалежно від його ширини. Тому розглядається масив з 9 елементів. 

    R - радіус півкола, утвореного при перетині даху. """
    array, R = np.zeros(9, dtype=float), 0

    while True:  # Введення значення змінної R
        try:
            R = float(input("Введіть радіус півкола:"))
            if R > 0:
                break
            else:
                print("Вводьте правильні дані!")
        except ValueError:
            print("Вводьте правильні дані!")

    for i in range(1, 10):  # Знаходження довжин опор даху
        array[i-1] = round(sqrt(R**2 - abs(i*R/5 - R)**2), 2)

    print("Значення довжин опор, що підтримують дах, який при перетині утворює "
          f"півколо радіуса {R}, дорівнює: ", end="")
    for i in range(9):  # Виведення даних масиву array
        print(array[i], "м", end="")
        if i != 8:
            print(", ", end="")
        else:
            print(".")

    answer = input("Введіть '1' для повторення:")
