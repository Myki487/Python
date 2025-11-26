import os
import sys
import traceback
from typing import List, Tuple, Dict

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from gensim import corpora
from gensim.models import LdaModel

import matplotlib.pyplot as plt

DEFAULT_INPUT = "documents.csv"
OUTPUT_TXT = "topic_modeling_results.txt"
OUTPUT_CSV = "document_topics.csv"
OUTPUT_PNG = "topics_top_words.png"


def ensure_nltk_resources():
    resources = ["punkt", "stopwords", "wordnet", "omw-1.4"]
    for r in resources:
        try:
            nltk.data.find(f"tokenizers/{r}") if r == "punkt" else nltk.data.find(f"corpora/{r}")
        except LookupError:
            print(f"Завантажую NLTK ресурс: {r} ...")
            nltk.download(r, quiet=True)


def create_sample_data(path: str = DEFAULT_INPUT):
    if os.path.exists(path):
        return
    data = {
        "doc_id": [1, 2, 3, 4, 5, 6],
        "text": [
            "Bitcoin and Ethereum are leading cryptocurrencies. Blockchain technology is fascinating.",
            "The stock market saw a dip yesterday due to interest rate hikes. Investing requires patience.",
            "My favorite sport is football, followed closely by basketball. I watch the Champions League every week.",
            "I enjoy trading stocks and reading financial news. The market is very volatile.",
            "I need to buy a new football and practice my shooting skills. Sports are healthy.",
            "Decentralized finance relies on smart contracts. Ethereum platform is highly scalable."
        ]
    }
    df = pd.DataFrame(data)
    df.to_csv(path, index=False, encoding="utf-8")
    print(f"Створено демонстраційний файл '{path}'.")


def load_data(path: str) -> pd.DataFrame:
    """Читає CSV з колонкою 'text' і 'doc_id' (якщо є)."""
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    if "text" not in df.columns:
        raise ValueError("CSV має містити колонку 'text'.")
    if "doc_id" not in df.columns:
        df.insert(0, "doc_id", range(1, 1 + len(df)))
    return df


def preprocess_texts(texts: List[str]) -> List[List[str]]:
    ensure_nltk_resources()
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))

    processed = []
    for text in texts:
        try:
            tokens = [t.lower() for t in nltk.word_tokenize(str(text))]
        except Exception:
            tokens = str(text).split()
        filtered = [
            lemmatizer.lemmatize(w)
            for w in tokens
            if w.isalpha() and w not in stop_words and len(w) > 2
        ]
        processed.append(filtered)
    return processed


def build_dictionary_corpus(processed_texts: List[List[str]]) -> Tuple[corpora.Dictionary, List[List[Tuple[int, int]]]]:
    dictionary = corpora.Dictionary(processed_texts)
    dictionary.filter_extremes(no_below=1, no_above=0.9)
    corpus = [dictionary.doc2bow(doc) for doc in processed_texts]
    return dictionary, corpus


def train_lda(corpus, dictionary, num_topics: int) -> LdaModel:
    model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        random_state=42,
        update_every=1,
        chunksize=100,
        passes=15,
        alpha='auto',
        per_word_topics=False
    )
    return model


def get_topic_top_words(lda_model: LdaModel, topn: int = 10) -> Dict[int, List[Tuple[str, float]]]:
    topics = {}
    for tid in range(lda_model.num_topics):
        terms = lda_model.show_topic(tid, topn=topn)
        topics[tid] = terms
    return topics


def assign_main_topic_to_docs(lda_model: LdaModel, corpus) -> List[Tuple[int, float]]:
    doc_topics = []
    for bow in corpus:
        topics = lda_model.get_document_topics(bow)
        if topics:
            main = max(topics, key=lambda x: x[1])
            doc_topics.append((main[0], main[1]))
        else:
            doc_topics.append((-1, 0.0))
    return doc_topics


def save_results_txt(path_txt: str, num_topics: int, topics_dict: Dict[int, List[Tuple[str, float]]],
    doc_topic_assignments: List[Tuple[int, float]], df: pd.DataFrame):
    lines = []
    lines.append(f"Звіт про тематичне моделювання (LDA) - Кількість тем: {num_topics}\n")
    for tid, terms in topics_dict.items():
        term_str = " + ".join([f'{weight:.3f}*"{term}"' for term, weight in terms])
        lines.append(f"Тема #{tid + 1}: {term_str}")
    lines.append("\n" + "="*70 + "\n")
    lines.append("Призначення основної теми кожному документу:")
    for idx, (topic_id, prob) in enumerate(doc_topic_assignments):
        doc_id = df.at[idx, "doc_id"]
        if topic_id >= 0:
            lines.append(f"Документ #{doc_id} -> Тема #{topic_id + 1} (Впевненість: {prob:.2f})")
        else:
            lines.append(f"Документ #{doc_id} -> Тема не визначена.")
    with open(path_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Детальний звіт збережено у '{path_txt}'.")


def save_results_csv(path_csv: str, df: pd.DataFrame, doc_topic_assignments: List[Tuple[int, float]]):
    df_out = df.copy()
    df_out["assigned_topic"] = [t + 1 if t >= 0 else None for t, _ in doc_topic_assignments]
    df_out["topic_probability"] = [prob for _, prob in doc_topic_assignments]
    df_out.to_csv(path_csv, index=False, encoding="utf-8")
    print(f"CSV з результатами збережено у '{path_csv}'.")


def plot_top_words(topics: Dict[int, List[Tuple[str, float]]], out_png: str):
    labels = []
    weights = []
    topic_ids = []
    for tid, terms in topics.items():
        for term, weight in terms:
            labels.append(f"{term}\n(t{tid+1})")
            weights.append(weight)
            topic_ids.append(tid+1)
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(weights)), weights)
    plt.xticks(range(len(weights)), labels, rotation=45, ha="right")
    plt.title("Top words per topic")
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()
    print(f"Графік топ-слів збережено у '{out_png}'.")


def interactive_dialog():
    print("=== ЗАВДАННЯ 2: ТЕМАТИЧНЕ МОДЕЛЮВАННЯ (LDA) ===")
    try:
        inp = input(f"Введи шлях до CSV-файлу з документами або натисни Enter для '{DEFAULT_INPUT}': ").strip()
        input_path = inp if inp else DEFAULT_INPUT

        gen = input("Створити демонстраційний файл якщо відсутній? (y/n) [y]: ").strip().lower() or "y"
        if gen == "y":
            create_sample_data(input_path)

        try:
            df = load_data(input_path)
        except FileNotFoundError:
            print(f"Файл '{input_path}' не знайдено. Сканую директорію і пропоную створити демонстраційний.")
            create_sample_data(input_path)
            df = load_data(input_path)

        num_topics_raw = input("Кількість тем для моделювання (ціле число) [3]: ").strip() or "3"
        try:
            num_topics = max(1, int(num_topics_raw))
        except ValueError:
            print("Некоректне число тем, використовую 3.")
            num_topics = 3

        show_steps = True
        print("Етап 1/4: Очищення та підготовка тексту...")
        processed = preprocess_texts(df["text"].tolist())

        print("Етап 2/4: Створення словника та корпусу Gensim...")
        dictionary, corpus = build_dictionary_corpus(processed)

        if not dictionary.token2id:
            raise RuntimeError("Після фільтрації словника не залишилось токенів. Перевірте вхідні документи.")

        print(f"Етап 3/4: Навчання моделі LDA на {num_topics} темах...")
        lda_model = train_lda(corpus, dictionary, num_topics)

        print("Етап 4/4: Виведення та збереження результатів...")
        topics = get_topic_top_words(lda_model, topn=10)
        assignments = assign_main_topic_to_docs(lda_model, corpus)

        save_results_txt(OUTPUT_TXT, num_topics, topics, assignments, df)
        save_results_csv(OUTPUT_CSV, df, assignments)

        want_plot = input("Зберегти графік топ-слів (PNG)? (y/n) [y]: ").strip().lower() or "y"
        if want_plot == "y":
            plot_top_words(topics, OUTPUT_PNG)

        print("\nКороткий огляд тем (топ-3 слів):")
        for tid, terms in topics.items():
            top3 = ", ".join([t for t, _ in terms[:3]])
            print(f"Тема #{tid + 1}: {top3}")

        print("\nГотово.")

    except ModuleNotFoundError as me:
        print("Помилка: не знайдено потрібну бібліотеку. Виконай:\n    python -m pip install gensim nltk pandas matplotlib")
        print(me)
        sys.exit(1)
    except Exception as e:
        print("\nОбробка виключення: Виникла помилка:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    interactive_dialog()
