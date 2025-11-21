import pandas as pd
import numpy as np

data = {
    "Учень": ["Vitaly", "Dmytro", "Mikhail", "Maxim", "Victoria", "Anna", "Serhiy", "Olena"],
    "Оцінка_1": [12, 12, 3, 5, 10, 11, 8, 9],
    "Оцінка_2": [10, 12, 4, 5, 10, 10, 7, 8],
    "Оцінка_3": [11, 12, 3, 6, 10, 12, 9, 9],
    "Оцінка_4": [9, 11, 4, 4, 9, 11, 8, 7],
    "Оцінка_5": [12, 11, 3, 5, 10, 10, 7, 8],
    "Кількість_Товару": [1, 5, 2, 4, 3, 1, 5, 2],
    "Ціна_Товару_грн": [15000, 8000, 12000, 9500, 20000, 16000, 7500, 18000],
    "Категорія_Товару": ["Premium", "Standard", "Premium", "Standard", "Premium", "Premium", "Standard", "Premium"]
}

df = pd.DataFrame(data)

print("Словник перетворено на DataFrame")
print(df)
print("\n" + "="*50)

print("=== 2. Базовий Аналіз Даних ===")
print("\nа) Перші 3 рядки DataFrame (df.head(3)):")
print(df.head(3))

print("\nб) Типи даних (df.dtypes):")
print(df.dtypes)

print("\nв) Розмір DataFrame (df.shape):")
print(f"Кількість рядків і стовпців: {df.shape}")

print("\nг) Описова статистика (df.describe()):")
print(df.describe())

print("\n" + "="*50)

print("=== 3. Операції Фільтрації, Сортування та Розрахунків ===")

df['Загальна_Вартість_Продажу'] = df['Кількість_Товару'] * df['Ціна_Товару_грн']
print("\nа) DataFrame після додавання стовпця 'Загальна_Вартість_Продажу':")
print(df[['Учень', 'Ціна_Товару_грн', 'Кількість_Товару', 'Загальна_Вартість_Продажу']].head())

df_filtered = df[df['Ціна_Товару_грн'] > 10000]
print("\nб) Фільтрація: Записи з 'Ціна_Товару_грн' > 10000:")
print(df_filtered[['Учень', 'Ціна_Товару_грн']])

df_sorted = df.sort_values(by='Ціна_Товару_грн', ascending=False)
print("\nв) Сортування: Записи за спаданням 'Ціна_Товару_грн':")
print(df_sorted[['Учень', 'Ціна_Товару_грн']].head())

print("\n" + "="*50)

print("=== 4. Групування та Агрегація ===")

df_grouped_mean = df.groupby('Категорія_Товару')['Ціна_Товару_грн'].mean()
print("\nа) Групування та Середнє значення: Середня ціна товару за 'Категорією_Товару':")
print(df_grouped_mean)

print("\nб) Додаткові операції агрегації:")

max_sales_by_category = df.groupby('Категорія_Товару')['Загальна_Вартість_Продажу'].max()
print("   - Максимальна загальна вартість продажу (Max Sum) за категорією:")
print(max_sales_by_category)

unique_categories_count = df['Категорія_Товару'].nunique()
print(f"\n   - Кількість унікальних категорій товару (nunique): {unique_categories_count}")