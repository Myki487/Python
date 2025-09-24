def removeLetters(word):
    if len(word) < 2:
        return word
    newWord = word[0]
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            newWord += word[i]
    return newWord


while True:
    print("\n--- Завдання 2 ---")
    word = str(input("Введіть слово для оброблення (мін. 2 символи): "))
    if len(word) >= 2:
        resultWord = removeLetters(word)
        print(f"Початкове слово: {word}")
        print(f"Оброблене слово: {resultWord}")
    else:
        print("Помилка: Вам потрібно ввести рядок щонайменше з 2 символів.")

    answer = input("Бажаєте спробувати ще раз? (так/ні): ").lower()
    if answer != "так":
        break
