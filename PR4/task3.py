task_number = "Завдання №3"
print(task_number)

def process_list():
    input_str = input("Введіть елементи списку, розділені пробілами: ")
    if not input_str.strip():
        print("Помилка валідації: Список не може бути порожнім.")
        return

    original_list = input_str.split()
    
    even_index_elements = []
    i = 0
    while i < len(original_list):
        even_index_elements.append(original_list[i])
        i += 2

    new_list = original_list + even_index_elements
    
    print("Початковий список:", original_list)
    print("Елементи з парними індексами:", even_index_elements)
    print("Оновлений список:", new_list)

process_list()