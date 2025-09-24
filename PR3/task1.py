def removeLetters(word):
    if len(word) < 4:
        return word
    newWord = word[1] + word[-2]
    return newWord


while True:
    print("\n--- Завдання 1 ---")
    word = str(input("Введіть слово для зрізу (мін. 4 символи): "))
    if len(word) >= 4:
        resultWord = removeLetters(word)
        print(f"Початкове слово: {word}")
        print(f"Зрізане слово: {resultWord}")
    else:
        print("Помилка: Вам потрібно ввести рядок щонайменше з 4 символів.")

    answer = input("Бажаєте спробувати ще раз? (так/ні): ").lower()
    if answer != "так":
        break
