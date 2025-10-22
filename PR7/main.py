task_number = "Завдання: Робота з текстовими файлами (Варіант 16)"
print(task_number)

FILE1_NAME = "TF19_1.txt"
FILE2_NAME = "TF19_2.txt"

def open_file_safe(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except Exception:
        print(f"Помилка: Файл {file_name} не вдалося відкрити у режимі '{mode}'.")
        return None
    else:
        print(f"Файл {file_name} успішно відкрито у режимі '{mode}'.")
        return file

def create_initial_file(file_name):
    initial_content = [
        "Це рядок з   багатьма пробілами та к о словами   з однією буквою.",
        "Другий   рядок: а б в г д e f,  а також довгі слова.",
        "Рядок три  і знову пробіли та л м н.",
        "Кінець."
    ]
    
    file = open_file_safe(file_name, "w")
    if file:
        try:
            for line in initial_content:
                file.write(line + '\n')
            print(f"Створено файл {file_name} та записано початкові дані.")
        except Exception:
            print(f"Помилка при записі даних у файл {file_name}.")
        finally:
            file.close()

def process_and_save_file(input_file_name, output_file_name):
    file_in = open_file_safe(input_file_name, "r")
    file_out = open_file_safe(output_file_name, "w")
    
    if file_in and file_out:
        try:
            for line in file_in:
                words = line.split()
                filtered_words = [word for word in words if len(word) > 1]
                processed_line = " ".join(filtered_words)
                file_out.write(processed_line + '\n')
            
            print(f"Вміст {input_file_name} оброблено, результат записано у {output_file_name}.")
            
        except Exception:
            print("Виникла помилка під час обробки та запису даних.")
            
        finally:
            file_in.close()
            file_out.close()
            print(f"Файли {input_file_name} та {output_file_name} закрито.")
    else:
        if file_in: file_in.close()
        if file_out: file_out.close()

def print_file_content(file_name):
    print("\n--- Вміст обробленого файла ---")
    file = open_file_safe(file_name, "r")
    if file:
        try:
            for line in file:
                print(line.rstrip())
        except Exception:
            print(f"Помилка при читанні файла {file_name}.")
        finally:
            file.close()
            print(f"Файл {file_name} закрито.")
    print("--------------------------------")

create_initial_file(FILE1_NAME)
process_and_save_file(FILE1_NAME, FILE2_NAME)
print_file_content(FILE2_NAME)
