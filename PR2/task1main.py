task_number = "Завдання №1"
print(task_number)

import math

def calculate_z():
    while True:
        try:
            m_str = input("Введіть число m (m >= 0) для обчислення z = sqrt(m) + 10: ")
            m = float(m_str)
        except ValueError:
            print("Помилка валідації: Введене значення не є числовим.")
            continue
        
        if m < 0:
            print("Помилка валідації: Число m не може бути від'ємним для квадратного кореня.")
            continue
            
        z = math.sqrt(m) + 10
        print(f"Результат функції 1: z = {z}")
        return

def calculate_average_even():
    while True:
        try:
            x_str = input("Введіть ціле число x: ")
            y_str = input("Введіть ціле число y: ")
            x = int(x_str)
            y = int(y_str)
        except ValueError:
            print("Помилка валідації: Введені значення мають бути цілими числами.")
            continue

        if x > y:
            x, y = y, x

        sum_even = 0
        count_even = 0
        
        for num in range(x, y + 1):
            if num % 2 == 0:
                sum_even += num
                count_even += 1
        
        if count_even > 0:
            average = sum_even / count_even
            print(f"Результат функції 2 (Середнє арифметичне): {average}")
            return
        else:
            print("Помилка: У заданому діапазоні немає парних чисел.")
            return

print("\n--- Виконання функції 1 ---")
calculate_z()

print("\n--- Виконання функції 2 ---")
calculate_average_even()
