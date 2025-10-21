import math

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
