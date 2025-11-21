import nltk
import matplotlib.pyplot as plt
import string
from nltk.corpus import stopwords

TEXT_FILE = 'shakespeare-hamlet.txt'
PLOT_COLOR_1 = 'skyblue'
PLOT_COLOR_2 = 'salmon'

def ensure_nltk_downloads():
    print("--- Перевірка та завантаження ресурсів NLTK ---")
    
    required_packages = ['gutenberg', 'punkt', 'stopwords', 'punkt_tab']
    for package in required_packages:
        if package in ['punkt', 'punkt_tab']:
            resource_path = f'tokenizers/{package}'
        else:
            resource_path = f'corpora/{package}'
            
        try:
            nltk.data.find(resource_path)
            print(f"Пакет '{package}' вже встановлено.")
        except LookupError:
            print(f"Завантажуємо пакет '{package}'...")
            try:
                nltk.download(package, quiet=True)
                print(f"Пакет '{package}' успішно завантажено.")
            except Exception as e:
                print(f"Помилка завантаження '{package}': {e}")
                
    print("Ресурси NLTK готові.")


def load_and_analyze_text(file_id):
    try:
        raw_text = nltk.corpus.gutenberg.raw(file_id)
    except LookupError:
        print(f"Помилка: Корпус '{file_id}' не знайдено. Переконайтесь, що пакет 'gutenberg' завантажено.")
        return
    except Exception as e:
        print(f"Помилка при завантаженні тексту: {e}")
        return

    print(f"\n--- Аналіз тексту: {file_id} ---")
    
    tokens = nltk.word_tokenize(raw_text)
    total_words = len(tokens)
    print(f"1. Загальна кількість токенів (слів і пунктуації) у тексті: {total_words}")
    print("-" * 70)

    fdist_raw = nltk.FreqDist(tokens)
    top_10_raw = fdist_raw.most_common(10)
    
    print("2. 10 найбільш вживаних токенів (включаючи пунктуацію):")
    for word, count in top_10_raw:
        print(f"   - {word}: {count}")

    plot_frequency(top_10_raw, "10 найбільш вживаних токенів (без фільтрації)", "raw_top_10_plot.png", PLOT_COLOR_1)
    
    print("\n" + "=" * 70)

    english_stopwords = set(stopwords.words('english'))
    punctuation_set = set(string.punctuation)

    filtered_tokens = [
        word.lower() 
        for word in tokens 
        if word.lower() not in english_stopwords and word not in punctuation_set and word.isalpha()
    ]
    
    fdist_filtered = nltk.FreqDist(filtered_tokens)
    top_10_filtered = fdist_filtered.most_common(10)

    print(f"Кількість токенів після фільтрації: {len(filtered_tokens)}")
    print("\n3. 10 найбільш вживаних слів (після видалення стоп-слів та пунктуації):")
    for word, count in top_10_filtered:
        print(f"   - {word}: {count}")

    plot_frequency(top_10_filtered, "10 найбільш вживаних слів (після фільтрації)", "filtered_top_10_plot.png", PLOT_COLOR_2)
    
    print("\n--- Аналіз NLTK завершено ---")


def plot_frequency(data, title, filename, color):
    words = [item[0] for item in data]
    counts = [item[1] for item in data]

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color=color)
    plt.title(title, fontsize=14)
    plt.xlabel('Слово', fontsize=12)
    plt.ylabel('Кількість вживань', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    plt.savefig(filename)
    print(f"   Графік '{title}' збережено як '{filename}'")

if __name__ == "__main__":
    ensure_nltk_downloads()
    load_and_analyze_text('shakespeare-hamlet.txt')