MIN_GRADE = 1
MAX_GRADE = 12

def print_separator():
    print("-" * 50)

def print_dictionary(students):
    print_separator()
    print("Вміст словника:")
    if not students:
        print("Словник порожній.")
        return
    for name, grades in students.items():
        print(f"Оцінки {name:<20} - {grades}")

def get_valid_key(students, action):
    while True:
        key = input(f"Введіть прізвище та ім'я учня для {action}: ").strip()
        if not key:
            print("Помилка: Прізвище та ім'я не можуть бути порожніми.")
            continue
        if action == "додавання" and key in students:
            print(f"Помилка: Учень {key} вже існує у словнику.")
            continue
        if action == "видалення" and key not in students:
            print(f"Помилка: Учень {key} не знайдений у словнику. Спробуйте ще раз.")
            continue
        return key

def get_valid_grades():
    while True:
        grades_input = input(f"Введіть оцінки через кому (від {MIN_GRADE} до {MAX_GRADE}, наприклад, 12,10,9): ")
        try:
            grades = [int(g.strip()) for g in grades_input.split(',') if g.strip()]
            if not grades:
                print("Помилка: Список оцінок не може бути порожнім.")
                continue
            if any(not (MIN_GRADE <= g <= MAX_GRADE) for g in grades):
                print(f"Помилка валідації: Усі оцінки мають бути цілими числами в діапазоні від {MIN_GRADE} до {MAX_GRADE}.")
                continue
            return grades
        except ValueError:
            print("Помилка валідації: Оцінки мають бути цілими числами, розділеними комами.")
        except Exception:
            print("Невідома помилка при введенні оцінок.")

def add_entry(students):
    print_separator()
    name = get_valid_key(students, "додавання")
    grades = get_valid_grades()
    students[name] = grades
    print(f"Додано запис для учня {name}.")

def delete_entry(students):
    print_separator()
    if not students:
        print("Словник порожній. Нічого видаляти.")
        return
    
    name = get_valid_key(students, "видалення")
    try:
        del students[name]
        print(f"Видалено запис для учня {name}.")
    except KeyError:
        print(f"Виключна ситуація: Учень {name} не знайдений. Видалення не відбулося.")

def print_sorted_keys(students):
    print_separator()
    if not students:
        print("Словник порожній.")
        return
    
    sorted_keys = sorted(students.keys())
    print("Вміст словника за відсортованими ключами:")
    for name in sorted_keys:
        print(f"Оцінки {name:<20} - {students[name]}")

def find_best_and_worst_student(students):
    print_separator()
    if not students:
        print("Словник порожній. Неможливо виконати аналіз.")
        return
    
    total_scores = {name: sum(grades) for name, grades in students.items()}
    
    if not total_scores:
        print("Немає даних для аналізу.")
        return

    max_score = -1
    max_students = []
    min_score = float('inf')
    min_students = []

    for name, score in total_scores.items():
        # Найбільша сума
        if score > max_score:
            max_score = score
            max_students = [name]
        elif score == max_score:
            max_students.append(name)

        # Найменша сума
        if score < min_score:
            min_score = score
            min_students = [name]
        elif score == min_score:
            min_students.append(name)
            
    # Вивід результатів
    print("\nАналіз оцінок:")
    
    print(f"а) Учень(ні), який(і) має(ють) найбільшу суму оцінок ({max_score}):")
    for name in max_students:
        print(f"   - {name}")

    print(f"б) Учень(ні), який(і) має(ють) найменшу суму оцінок ({min_score}):")
    for name in min_students:
        print(f"   - {name}")

def main():
    students = {
        "Vitaly": [12, 10, 11, 9, 12], 
        "Dmytro": [12, 12, 12, 11, 11], 
        "Mikhail": [3, 4, 3, 4, 3], 
        "Maxim": [5, 5, 6, 4, 5], 
        "Victoria": [10, 10, 10, 9, 10], 
    }
    
    while True:
        print_separator()
        print("Меню роботи зі словником оцінок:")
        print("1 - Вивести всі значення словника")
        print("2 - Додати запис студента")
        print("3 - Видалити запис студента")
        print("4 - Переглянути вміст за відсортованими ключами")
        print("5 - Знайти учня з найбільшою/найменшою сумою оцінок")
        print("0 - Вийти з програми")
        print_separator()
        
        choice = input("Введіть пункт меню: ").strip()
        
        if choice == '1':
            print_dictionary(students)
        elif choice == '2':
            add_entry(students)
        elif choice == '3':
            delete_entry(students)
        elif choice == '4':
            print_sorted_keys(students)
        elif choice == '5':
            find_best_and_worst_student(students)
        elif choice == '0':
            print("Завершення програми.")
            break
        else:
            print("Помилка: Невірний пункт меню. Спробуйте ще раз.")
            
        input("\nНатисніть Enter, щоб продовжити...")

if __name__ == "__main__":
    main()