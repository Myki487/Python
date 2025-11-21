import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = 'comptagevelo2013.csv'
SELECTED_YEAR = 2013

def analyze_bike_traffic(file_name):
    try:
        df = pd.read_csv(file_name, parse_dates=['Date'])
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_name}' не знайдено. Переконайтесь, що він знаходиться в тій же папці.")
        return
    except Exception as e:
        print(f"Помилка при читанні файлу CSV: {e}")
        return

    print(f"--- Аналіз Даних Велодоріжок за {SELECTED_YEAR} рік ---")

    print("\nа) Перші 5 рядків (df.head()):")
    print(df.head())

    print("\nб) Інформація про DataFrame (df.info()):")
    df.info(verbose=False, memory_usage="deep")

    print("\nв) Описова статистика (df.describe()):")
    print(df.describe())

    print("\n" + "="*70)

    df = df.set_index('Date')
    
    traffic_columns = df.columns
    print(f"Виявлені велодоріжки: {', '.join(traffic_columns)}")
    print("\n" + "-"*70)

    total_annual_traffic = df[traffic_columns].sum().sum()
    print(f"3.1. Загальна кількість велосипедистів за {SELECTED_YEAR} рік на усіх доріжках: {total_annual_traffic} велосипедистів")

    print("\n" + "-"*70)

    annual_traffic_by_lane = df[traffic_columns].sum(axis=0).sort_values(ascending=False)
    print("3.2. Загальна кількість велосипедистів за рік на кожній велодоріжці:")
    print(annual_traffic_by_lane)

    print("\n" + "-"*70)

    selected_lanes = traffic_columns[:3] 
    
    if len(selected_lanes) < 3:
        print(f"⚠️ У файлі знайдено лише {len(traffic_columns)} доріжок. Аналізуємо усі.")
        selected_lanes = traffic_columns
    
    df['Місяць'] = df.index.month_name()

    monthly_traffic = df.groupby('Місяць')[selected_lanes].sum()
    
    print("3.3. Аналіз популярності місяців на обраних доріжках:")
    for lane in selected_lanes:
        most_popular_month = monthly_traffic[lane].idxmax()
        max_count = monthly_traffic[lane].max()
        print(f"   - Дорожка '{lane}': Найбільш популярний місяць - {most_popular_month} ({max_count} велосипедистів)")

    print("\n" + "="*70)
    print("--- Побудова графіку завантаженості ---")

    lane_to_plot = traffic_columns[0] 
    monthly_traffic_for_plot = df.groupby(df.index.to_period('M'))[lane_to_plot].sum()
    plt.style.use('seaborn-v0_8-deep')
    plt.figure(figsize=(10, 6))
    monthly_traffic_for_plot.plot(kind='bar', color='darkgreen')

    plt.title(f'Завантаженість велодоріжки {lane_to_plot} по місяцях ({SELECTED_YEAR} рік)', fontsize=14)
    plt.xlabel('Місяць (Рік)', fontsize=12)
    plt.ylabel('Загальна кількість велосипедистів', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()

    plot_filename = f'bike_lane_traffic_{SELECTED_YEAR}_analysis.png'
    plt.savefig(plot_filename)
    print(f"Графік успішно побудовано та збережено як '{plot_filename}'")

if __name__ == "__main__":
    analyze_bike_traffic(INPUT_FILE)