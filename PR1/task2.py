task_number = "Завдання №2"
print(task_number)

INITIAL_AMOEBA = 1
DIVISION_FACTOR = 3
DIVISION_INTERVAL = 2
REPORT_START_HOUR = 12
REPORT_END_HOUR = 48
REPORT_STEP = 12

print("Година | Кількість амеб")
print("-----------------------")

amoebas = INITIAL_AMOEBA
current_hour = 0
report_hour = REPORT_START_HOUR

while current_hour <= REPORT_END_HOUR:
    if current_hour > 0 and current_hour % DIVISION_INTERVAL == 0:
        amoebas *= DIVISION_FACTOR

    if current_hour == report_hour:
        print(f"{current_hour:6} | {amoebas}")
        report_hour += REPORT_STEP

    current_hour += 1
