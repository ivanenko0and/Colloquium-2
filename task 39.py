
"""
Дані про температуру повітря і кількості опадів за декаду квітня зберігаються в масивах.
Визначити кількість опадів, що випали у вигляді дощу і у вигляді снігу за цю декаду.

Виконав Іваненко Андрій Вадимович
"""

import numpy as np

answer = '1'
while answer == '1':

    """ temperature_array - масив, що містить результати щоденного вимірювання температури повітря протягом квітня.
    Значення temperature_array - 30 випадкових чисел від -20 до 20.
    
    precipitation_array - масив, який містить дані щодо кількості опадів, які випали протягом місяця квітня.
    Значення precipitation_array - 30 випадкових чисел від 0 до 30.
    
    rain - кількість опадів за декаду квітня, що випали у вигляді дощу.
    snow - кількість опадів за декаду квітня, що випали у вигляді снігу. """
    temperature_array, precipitation_array = np.random.randint(-20, 20, 30), np.random.randint(0, 30, 30)
    rain, snow = 0, 0

    print("Дані про температуру повітря і кількість опадів за місяць квітень: ")
    for i in range(30):  # Виведення даних масивів temperature_array і precipitation_array
        print(f"{i + 1} квітня: {temperature_array[i]} °C; {precipitation_array[i]} мм опадів.")

        if temperature_array[i] > 0:  # Підрахунок значень rain і snow
            rain += precipitation_array[i]
        else:
            snow += precipitation_array[i]
    print(f"Протягом місяця випало {rain} мм дощу та {snow} мм снігу.")  # Виведення значень rain і snow

    answer = input("Введіть '1' для повторення:")
