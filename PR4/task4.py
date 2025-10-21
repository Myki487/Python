task_number = "Завдання №4"
print(task_number)

def find_duplicates():
    input_str = input("Введіть елементи списку, розділені пробілами: ")
    if not input_str.strip():
        print("Помилка валідації: Список не може бути порожнім.")
        return

    original_list = input_str.split()
    
    seen = set()
    duplicates = set()

    for item in original_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    new_list = list(duplicates)

    print("Початковий список:", original_list)
    print("Новий список з елементами, що повторюються:", new_list)

find_duplicates()
