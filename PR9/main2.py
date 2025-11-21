import json
import os
from collections import defaultdict
import sys
1
INPUT_FILENAME = 'grades.json'
OUTPUT_FILENAME = 'results_grades.json'

def load_data(filename=INPUT_FILENAME):
    """Завантажує дані з JSON-файлу або створює його, якщо він не існує."""
    if not os.path.exists(filename):
        print(f"Файл '{filename}' не знайдено. Створюємо його з початковими даними...")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(INITIAL_DATA, f, ensure_ascii=False, indent=4)
        return INITIAL_DATA
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                print(f"Помилка: Файл '{filename}' містить невірний формат даних.")
                return []
            return data
    except json.JSONDecodeError:
        print(f"Помилка: Файл '{filename}' містить недійсний JSON.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

def save_data(data, filename=INPUT_FILENAME):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Дані успішно збережено у файл '{filename}'.")
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")

def display_data(data):
    if not data:
        print("База даних порожня або не завантажена.")
        return
    print("\nВміст JSON-файлу")
    print(json.dumps(data, ensure_ascii=False, indent=4))
    print("-----------------------------------")

def add_entry(data):
    print("\nДодавання нового учня...")
    surname = input("Введіть прізвище учня: ").strip()
    if not surname:
        print("Прізвище не може бути порожнім.")
        return
    new_grades = {}
    subjects = ["Математика", "Історія", "Фізика", "Інформатика", "Англійська"]
    print("Введіть оцінки (за 5-бальною шкалою):")
    for subject in subjects:
        while True:
            try:
                grade = int(input(f"Оцінка з {subject}: "))
                if 1 <= grade <= 5:
                    new_grades[subject] = grade
                    break
                else:
                    print("Оцінка має бути у діапазоні від 1 до 5.")
            except ValueError:
                print("Некоректний ввід. Введіть число.")
    new_entry = {"Прізвище": surname, "Оцінки": new_grades}
    data.append(new_entry)
    save_data(data)

def delete_entry(data):
    print("\nВидалення учня...")
    surname_to_delete = input("Введіть прізвище учня для видалення: ").strip()
    initial_length = len(data)
    new_data = [entry for entry in data if entry.get("Прізвище") != surname_to_delete]
    if len(new_data) < initial_length:
        print(f"Учня '{surname_to_delete}' успішно видалено.")
        save_data(new_data)
        data[:] = new_data
    else:
        print(f"Учня '{surname_to_delete}' не знайдено.")

def search_data(data):
    print("\nПошук учня за прізвищем")
    search_surname = input("Введіть прізвище для пошуку: ").strip()
    found = False
    for entry in data:
        if entry.get("Прізвище") == search_surname:
            print(f"\nЗнайдено учня: {entry['Прізвище']}")
            print("Оцінки:")
            for subject, grade in entry['Оцінки'].items():
                print(f"  {subject}: {grade}")
            found = True
            break
    if not found:
        print(f"Учня з прізвищем '{search_surname}' не знайдено.")

def analyze_grades(data):
    if not data:
        print("База даних порожня. Аналіз неможливий.")
        return

    print("\nАналіз: Пошук Max/Min Суми Оцінок")
    
    max_sum = -1
    min_sum = sys.maxsize
    max_students = []
    min_students = []
    
    for student in data:
        surname = student.get("Прізвище", "N/A")
        current_sum = sum(student.get("Оцінки", {}).values())
        if current_sum > max_sum:
            max_sum = current_sum
            max_students = [(surname, current_sum)]
        elif current_sum == max_sum:
            max_students.append((surname, current_sum))
        if current_sum < min_sum:
            min_sum = current_sum
            min_students = [(surname, current_sum)]
        elif current_sum == min_sum:
            min_students.append((surname, current_sum))
    results = {
        "Найбільша_Сума_Оцінок": {
            "Сума": max_sum,
            "Учні": [s[0] for s in max_students]
        },
        "Найменша_Сума_Оцінок": {
            "Сума": min_sum,
            "Учні": [s[0] for s in min_students]
        }
    }
    print(f"Найбільша сума оцінок ({max_sum} балів): {', '.join(results['Найбільша_Сума_Оцінок']['Учні'])}")
    print(f"Найменша сума оцінок ({min_sum} балів): {', '.join(results['Найменша_Сума_Оцінок']['Учні'])}")
    save_data(results, OUTPUT_FILENAME)


def main_menu():
    data = load_data()
    while True:
        print("\n" + "="*50)
        print("=== МЕНЮ ОБРОБКИ JSON-ДАНИХ (ВАРІАНТ 16) ===")
        print("="*50)
        print("1. Вивести вміст JSON-файлу на екран")
        print("2. Додати новий запис (учня)")
        print("3. Видалити запис (учня)")
        print("4. Пошук даних за прізвищем")
        print("5. Розв’язання завдання (Max/Min сума оцінок)")
        print("0. Вихід")
        
        choice = input("Оберіть опцію (0-5): ")
        
        if choice == '1':
            display_data(data)
        elif choice == '2':
            add_entry(data)
        elif choice == '3':
            delete_entry(data)
        elif choice == '4':
            search_data(data)
        elif choice == '5':
            analyze_grades(data)
        elif choice == '0':
            print("Програма завершена. До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, оберіть число від 0 до 5.")

if __name__ == "__main__":
    main_menu()