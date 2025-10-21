N = 7
matrix = []
task_number = "Завдання №2"

print(task_number)

for i in range(N):
    row = []
    for j in range(N):
        value = j - i
        row.append(value)
    matrix.append(row)

for row in matrix:
    row_str = ""
    for value in row:
        row_str += f"{value:3} "
    print(row_str.strip())