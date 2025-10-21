def replaceLetters(word):
    if len(word) < 2:
        return word
    return word.replace('b', 'c').replace('B', 'C')

while True:
    print("\n--- Завдання 3 ---")
    word = str(input("Введіть слово для заміни літер b на c (мін. 2 символи): "))
    if len(word) >= 2:
        resultWord = replaceLetters(word)
        print(f"Початкове слово: {word}")
        print(f"Оброблене слово: {resultWord}")
    else:
        print("Помилка: Вам потрібно ввести рядок щонайменше з 2 символів.")

    answer = input("Бажаєте спробувати ще раз? (так/ні): ").lower()
    if answer not in ["так", "т", "yes", "y"]:
        break
