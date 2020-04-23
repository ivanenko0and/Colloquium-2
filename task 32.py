
"""
Змінній t привласнити значення істина, якщо в одновимірному масиві є хоча б одне від’ємне і парне число.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    array, t = np.random.randint(-10, 50, 20), False  # array - масив із 20 випадкових цілих чисел від -10 до 50
    # t - змінна, яка приймає значення істинності, якщо масив array містить хоча б одне від’ємне парне число

    print("Послідовність з 20 випадкових чисел дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")
        else:
            print(".")

        if array[i] % 2 == 0 and array[i] < 0:  # Пошук від’ємного парного числа у масиві array
            t = True

    if t:  # Вивід відповідного тексту
        print("Ця послідовність чисел містить в собі як мінімум одне від’ємне парне число.")
    else:
        print("Ця послідовність чисел не містить в собі ні одного від'ємного парного числа.")

    answer = input("Введіть '1' для повторення:")
