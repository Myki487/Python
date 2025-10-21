task_number = "Завдання №1"
print(task_number)

MIN_VAL = 1
MAX_VAL = 100

def get_valid_input(var_name):
    while True:
        try:
            value_str = input(f"Введіть значення {var_name} (від {MIN_VAL} до {MAX_VAL} включно): ")
            value = float(value_str)

            if not (MIN_VAL <= value <= MAX_VAL):
                print(f"Помилка валідації: {var_name} має бути в діапазоні від {MIN_VAL} до {MAX_VAL}.")
                continue
            
            return value
        except ValueError:
            print("Помилка валідації: Введене значення має бути числовим.")

a = get_valid_input("a")
b = get_valid_input("b")

x = None

if a < b:
    if a == 0:
        print("Помилка обчислення: Ділення на нуль (a=0).")
    else:
        x = (b / a) - 1
elif a == b:
    x = -295
elif a > b:
    if b == 0:
        print("Помилка обчислення: Ділення на нуль (b=0).")
    else:
        x = (a - 235) / b

if x is not None:
    print(f"При a = {a} та b = {b}, значення X = {x}")