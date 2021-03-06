
"""
Знайти суму всіх елементів масиву дійсних чисел, більших за задане число.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 50 до 100.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    """ array - масив із 20 випадкових дійсних чисел від 50 до 100.
    (Для створення масиву випадкових дійсних чисел використовується функція numpy.random.uniform(). Так як створені 
    таким чином числа мають занадто велику частину після крапки, то використовується функція map() з виконанням функції 
    round() для її скорочення. Оскільки повертається об'єкт типу map, який не розпізнається функцією numpy.array(), 
    то спочатку об'єкт перетворюється у список за допомогою list(), а вже потім застосовується numpy.array() для 
    перетворення у масив.)
    num_sum - сума всіх елементів масиву array, більших за задане число number. """
    array, num_sum = np.array(list(map(lambda x: round(x, 2), np.random.uniform(50, 100, 20)))), 0

    while True:  # Введення числа number
        try:
            number = float(input("Введіть число:"))
            break
        except ValueError:
            print("Вводьте правильні дані!")

    print("Послідовність з 20 випадкових дійсних чисел від 50 до 100 дорівнює: ", end="")
    for i in range(20):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 19:
            print(", ", end="")

        if array[i] > number:  # Знаходження суми всіх елементів масиву array, більших за задане число number
            num_sum += array[i]
    # Виведення значення num_sum
    print(f"\nСума всіх чисел послідовності, більших за число {number}, дорівнює: {round(num_sum, 2)}")

    answer = input("Введіть '1' для повторення:")
