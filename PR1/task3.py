task_number = "Завдання №3"
print(task_number)

def get_pyramid_size():
    MIN_N = 1
    MAX_N = 9
    while True:
        try:
            n_str = input(f"Введіть ціле число N ({MIN_N} < N < {MAX_N}): ")
            n = int(n_str)
        except ValueError:
            print("Помилка валідації: Введене значення не є цілим числом.")
            continue
        
        if not (MIN_N < n < MAX_N):
            print(f"Помилка валідації: N повинно бути більшим за {MIN_N} та меншим за {MAX_N}.")
            continue
        
        return n

n = get_pyramid_size()

for i in range(1, n + 1):
    row_str = ""
    for j in range(i, 0, -1):
        row_str += str(j)
        row_str += " "
    
    padding = "  " * (n - i)
    
    print(padding + row_str.rstrip())
