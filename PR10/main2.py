import os
import sys

try:
    import pandas as pd
except ImportError:
    print("Потрібно встановити pandas: pip install pandas")
    sys.exit(1)

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Потрібно встановити matplotlib: pip install matplotlib")
    sys.exit(1)


def find_csv(filename_candidates):
    for fname in filename_candidates:
        if os.path.isabs(fname):
            if os.path.exists(fname):
                return fname
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            p = os.path.join(script_dir, fname)
            if os.path.exists(p):
                return p
    return None


def load_data(path):
    df = pd.read_csv(path, encoding='utf-8-sig')
    if 'Рік' not in df.columns:
        raise ValueError("У CSV немає стовпця 'Рік'.")
    return df


def normalize_country_input(s):
    s = s.strip().lower()
    map_ukr = {'україна', 'украина', 'ukraine', 'ukr', 'ua'}
    map_usa = {'сша', 'сша', 'usa', 'us', 'united states', 'united states of america', 'america', 'сша'}
    if s in map_ukr:
        return 'Україна'
    if s in map_usa:
        return 'США'
    return None


def plot_line(df, col1='Україна', col2='США'):
    x = df['Рік'].astype(int).tolist()
    y1 = pd.to_numeric(df[col1], errors='coerce').tolist()
    y2 = pd.to_numeric(df[col2], errors='coerce').tolist()

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, marker='o', label=col1)
    plt.plot(x, y2, marker='o', label=col2)
    plt.title('Динаміка показника (population total) — {} та {}'.format(col1, col2))
    plt.xlabel('Рік')
    plt.ylabel('Населення (млн)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    outname = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'line_plot.png')
    plt.savefig(outname)
    print(f"Збережено лінійний графік: {outname}")
    plt.show()


def plot_bar_for_country(df, country_col):
    x = df['Рік'].astype(int).tolist()
    y = pd.to_numeric(df[country_col], errors='coerce').tolist()

    plt.figure(figsize=(12, 6))
    plt.bar(x, y)
    plt.title(f'Стовпчаста діаграма: {country_col}')
    plt.xlabel('Рік')
    plt.ylabel('Населення (млн)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    safe_name = country_col.replace(' ', '_')
    outname = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'bar_plot_{safe_name}.png')
    plt.savefig(outname)
    print(f"Збережено стовпчасту діаграму: {outname}")
    plt.show()


def main():
    candidates = [
        'population_total.csv',
        'PR10/population_total.csv',
        os.path.join('PR10', 'population_total.csv'),
    ]
    csv_path = find_csv(candidates)
    if not csv_path:
        print("CSV не знайдено. Помістіть 'population_total.csv' в ту ж папку, що і main2.py, або у підпапку PR10.")
        sys.exit(1)

    df = load_data(csv_path)

    required_cols = {'Рік', 'Україна', 'США'}
    if not required_cols.issubset(set(df.columns)):
        print("CSV повинен містити стовпці: 'Рік', 'Україна', 'США'. Знайдено:", df.columns.tolist())
        sys.exit(1)

    plot_line(df, col1='Україна', col2='США')

    prompt = ("Введіть назву країни для стовпчастої діаграми (наприклад: 'Україна' або 'США').\n"
              "Підтримувані варіанти: Україна / Ukraine / УКР ; США / USA / US / America.\n"
              "За замовчуванням натисніть Enter -> 'Україна': ")
    user = input(prompt)
    if user.strip() == '':
        country = 'Україна'
    else:
        mapped = normalize_country_input(user)
        if mapped is None:
            print("Невідома країна. Доступні: 'Україна' або 'США'. Вихід.")
            sys.exit(1)
        country = mapped

    plot_bar_for_country(df, country)


if __name__ == '__main__':
    main()
