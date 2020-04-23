"""
Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    """ array - масив із 20 випадкових цілих чисел від 1 до 50.
    t - змінна, яка приймає значення істинності, якщо максимальний елемент масиву array єдиний і не перевищує 
    наперед заданого числа а.
    max_num - максимальний елемент масиву array."""
    array, t, max_num = np.random.randint(1, 50, 20), False, 0

    while True:  # Введення числа а
        try:
            a = int(input("Введіть ціле число:"))
            break
        except ValueError:
            print("Вводьте правильні дані!")

    print("Послідовність з 20 випадкових чисел дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")
        else:
            print(".")

        if max_num == array[i]:  # Перевірка на наявність дублікатів максимального елементу масиву array
            t = False  # Якщо є дублікат максимального числа, змінна t приймає значення хибності
        if max_num < array[i]:  # Знаходження максимального елементу масиву array
            max_num = array[i]
            t = True  # При перезаписуванні значення max_num змінна t приймає значення істинності

    print(f"Максимальний елемент цієї послідовності дорівнює: {max_num}.")

    # Якщо максимальний елемент масиву array більший за задане число а, змінна t приймає значення хибності
    if max_num > a:
        t = False

    if t:  # Вивід відповідного тексту
        print(f"Максимальний елемент цієї послідовності чисел єдиний і не перевищує заданого числа {a}.")
    else:
        print(f"Максимальний елемент цієї послідовності чисел не єдиний або перевищує задане число {a}.")

    answer = input("Введіть '1' для повторення:")
