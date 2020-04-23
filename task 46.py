
"""
Задана таблиця назв товарів, що випускаються заводом. Визначте, чи повторюється в цій таблиці назва першого товару, і,
якщо повторюється, видаліть назву першого товару з таблиці.

Виконав Іваненко Андрій Вадимович
"""


answer = '1'
while answer == '1':

    array, is_duplicate = [], False  # array - список, що містить послідовність з назв товарів, що випускаються заводом
    # is_duplicate - змінна, яка є істинною, якщо перший товар з послідовності array повторюється

    print("Введіть послідовність з назв товарів, що випускаються заводом (до першого введеного пропуску):")
    while True:  # Введення даних у список array, до першого введеного пропуску
        item = input()

        if item == "" or item == " ":
            break

        array.append(item)

        if item == array[0] and len(array) != 1:  # Пошук дубліката першого елемента списку array
            is_duplicate = True

    if is_duplicate:  # Видалення першого елемента списку array, якщо він повторюється
        del array[0]

    print("Список товарів дорівнює: ")
    for i in array:  # Виведення даних списку array
        print(f"- {i};")

    answer = input("Введіть '1' для повторення:")
