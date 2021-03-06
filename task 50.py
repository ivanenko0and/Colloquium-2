
"""
У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів виграшних квитків.
Перевірте, чи є квиток з номером N виграшним.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    # array - масив із 10 номерів виграшних лотерейних білетів, що є випадковими цілими числами від 1 до 100
    array = np.random.randint(1, 100, 10)

    while True:  # Введення змінної N, що є номером обраного лотерейного білету
        try:
            N = int(input("Введіть номер лотерейного білету (від 1 до 100):"))
            if 1 <= N <= 100:
                break
            else:
                print("Вводьте правильні дані!")
        except ValueError:
            print("Вводьте правильні дані!")

    if N in array:  # Перевірка на наявність обраного білету у масиві виграшних білетів
        print("Ви обрали виграшний білет!")
    else:
        print("Ваш білет не є виграшним.")

    print("Список виграшних білетів: ", end="")
    for i in range(10):  # Виведення даних масиву array
        print(array[i], end="")
        if i != 9:
            print(", ", end="")
        else:
            print(".")

    answer = input("Введіть '1' для повторення:")
