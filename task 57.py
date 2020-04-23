
"""
Відомість на зарплату представлена як дві таблиці. Одна містить прізвища працівників цеху, а друга - їх зарплату за
поточний місяць. Знайдіть прізвище працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою заробітною платою. Видаліть з відомості
на зарплату відомості про працівника, зарплата якого мінімальна.

Виконав Іваненко Андрій Вадимович
"""


answer = '1'
while answer == '1':

    workers, salary = [], []  # workers - список, що містить послідовність із заданих імен працівників цеху
    # salary - список, що містить задані зарплати працівників цеху
    arithmetic_mean = 0  # arithmetic_mean - середня зарплата всіх працівників цеху
    max_salary, max_salary_index = [0, 0], [0, 0]  # max_salary - список з двох найбільших зарплат працівників цеху
    # max_salary_index - список з індексів двох найбільших зарплат працівників цеху

    print("Введіть послідовність з імен працівників цеху (до першого введеного пропуску):")
    while True:  # Введення даних у список workers, до першого введеного пропуску
        item = input()
        if item == "" or item == " ":
            break
        workers.append(item)

    print("Введіть заробітну плату цих робітників за місяць:")
    for i in range(len(workers)):  # Введення даних у список salary, залежно від довжини списку workers
        while True:
            try:
                item = int(input())
                if item > 0:
                    break
                else:
                    print("Вводьте правильні дані!")
            except ValueError:
                print("Вводьте правильні дані!")
        salary.append(item)

        arithmetic_mean += item  # Підрахунок значення arithmetic_mean

        if max_salary[1] < item:  # Знаходження другої найбільшої зарплати серед робітників
            max_salary[1] = item
            max_salary_index[1] = i

        """ Якщо зарплата, що на другому місці у списку найбільших зарплат, більша за зарплату, що на першому, 
        то вони міняються місцями. """
        if max_salary[1] > max_salary[0]:
            max_salary[0], max_salary[1], = max_salary[1], max_salary[0]
            max_salary_index[0], max_salary_index[1], = max_salary_index[1], max_salary_index[0]

    arithmetic_mean = round(arithmetic_mean / len(salary))  # Знаходження середньої зарплати працівників

    # min_difference - найменша різниця серед всіх зарплат між кількістю зарплати працівника і середньою зарплатою
    min_difference, min_difference_index = salary[0], 0  # min_difference_index - індекс зарплати з найменшою різницею

    # min_salary - найменша зарплата серед всіх працівників цеху
    min_salary, min_salary_index = salary[0], 0  # min_salary_index - індекс найменшої зарплати

    print("Список працівників разом з їх заробітними платами дорівнює:")
    for i in range(len(workers)):  # Виведення даних списків workers і salary
        print(f"{workers[i]} - {salary[i]} грн;")

        if min_difference > abs(arithmetic_mean - salary[i]):  # Знаходження значення min_difference
            min_difference = abs(arithmetic_mean - salary[i])
            min_difference_index = i

        if min_salary > salary[i]:  # Знаходження значення min_salary
            min_salary = salary[i]
            min_salary_index = i

    print(f"Зарплата працівника {workers[min_difference_index]} найменше відхиляється від середньої зарплати "
          f"всіх робітників за місяць у порівнянні із зарплатами інших працівників. "
          f"(Середня зарплата - {arithmetic_mean} грн)")

    print(f"Працівниками з найбільшими заробітними платами є: {workers[max_salary_index[0]]} і "
          f"{workers[max_salary_index[1]]}. Їх зарплати дорівнюють {max_salary[0]} і {max_salary[1]} грн.")

    del salary[min_salary_index]  # Видалення зі списків workers і salary працівника з найменшою зарплатою
    del workers[min_salary_index]
    print("Список працівників разом з їх заробітними платами, "
          "в якому видалили робітника з найменшою зарплатою, дорівнює:")
    for i in range(len(workers)):  # Виведення списків workers і salary, в яких видалили робітника з найменшою зарплатою
        print(f"{workers[i]} - {salary[i]} грн;")

    answer = input("Введіть '1' для повторення:")
