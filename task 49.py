
"""
Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки за ці послуги.
Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.

Виконав Іваненко Андрій Вадимович
"""


answer = '1'
while answer == '1':

    services, costs = [], []  # services - список, що містить послідовність з назв послуг
    # costs - список, що містить розцінки для послуг списку services

    print("Введіть послідовність з назв послуг (до першого введеного пропуску):")
    while True:  # Введення даних у список services, до першого введеного пропуску
        item = input()
        if item == "" or item == " ":
            break
        services.append(item)

    print("Введіть розцінки для цих послуг:")
    for i in range(len(services)):  # Введення даних у список costs, залежно від довжини списку services
        while True:
            try:
                item = int(input())
                if item > 0:
                    break
                else:
                    print("Вводьте правильні дані!")
            except ValueError:
                print("Вводьте правильні дані!")
        costs.append(item)

    print("Список послуг разом з їх цінами дорівнює: ")
    for i in range(len(services)):  # Виведення даних списків services і costs
        print(f"{services[i]} - {costs[i]} грн;")


    while True:  # Введення значення змінної G
        try:
            G = int(input("Введіть ціну:"))
            if G > 0:
                break
            else:
                print("Вводьте правильні дані!")
        except ValueError:
            print("Вводьте правильні дані!")

    if G in costs:  # Якщо у списку costs існує елемент, що дорівнює G, виконується видалення всіх передуючих елементів

        G_index = 0  # G_index - номер елементу списку costs, який дорівнює G

        for i in range(len(services)):  # Пошук елементу списку costs, який дорівнює G
            if costs[i] == G:
                G_index = i

        # Видалення всіх елементів списків costs і services, індекси яких менші за номер елементу, що дорівнює G
        del costs[0: G_index]
        del services[0: G_index]

        print(f"Список послуг разом з їх цінами, які розташовані після послуги з розцінкою {G} грн:")
        for i in range(len(services)):  # Виведення даних списків services і costs
            print(f"{services[i]} - {costs[i]} грн;")

    else:
        print(f"Список послуг не містить в собі послуги, яка має ціну {G} грн.")

    answer = input("Введіть '1' для повторення:")
