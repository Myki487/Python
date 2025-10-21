def get_array_size():
    while True:
        try:
            size = int(input("Введіть довжину масиву (ціле, додатне число): "))
            if size > 0:
                return size
            else:
                print("Помилка: довжина масиву має бути більшою за 0.")
        except ValueError:
            print("Помилка: будь ласка, введіть ціле число.")

def get_array_elements(size):
    array = []
    print(f"Введіть {size} дійсних елементів масиву (можна вводити дробові числа):")
    for i in range(size):
        while True:
            try:
                element = float(input(f"Елемент {i + 1}: "))
                array.append(element)
                break
            except ValueError:
                print("Помилка: будь ласка, введіть дійсне число (наприклад, 10 або -5.5).")
    return array

def find_max_negative(array):
    negative_elements = [num for num in array if num < 0]
    
    if not negative_elements:
        return None
    else:
        return max(negative_elements)

def main():
    while True:
        print("\n--- Завдання №1 ---")
        
        array_size = get_array_size()
        user_array = get_array_elements(array_size)
        max_negative = find_max_negative(user_array)
        
        print("-" * 25)
        print(f"Введений вами масив: {user_array}")
        
        if max_negative is not None:
            print(f"Максимальний від’ємний елемент: {max_negative}")
        else:
            print("В масиві немає від’ємних елементів.")
        print("-" * 25)

        answer = input("Бажаєте виконати завдання ще раз? (так/ні): ").lower()
        if answer not in ["так", "т", "yes", "y"]:
            print("Дякую за роботу! Вихід...")
            break

if __name__ == "__main__":
    main()
