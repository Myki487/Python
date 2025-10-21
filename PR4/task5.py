task_number = "Завдання №5"
print(task_number)

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def set_operations():
    try:
        x = set(range(8, 23))
        
        y = set()
        i = 8
        while i <= 22:
            if is_prime(i):
                y.add(i)
            i += 1
    except Exception as e:
        print("Помилка при створенні множин:", e)
        return

    print("Множина X (цілі числа від 8 до 22):", x)
    print("Множина Y (прості числа):", y)
    
    try:
        z = x - y
    except TypeError:
        print("Помилка: Операція над множинами неможлива. Перетворення...")
        z_list = list(x)
        z = set(z_list)

    print("Множина Z (X - Y, непрості числа):", z)

set_operations()
