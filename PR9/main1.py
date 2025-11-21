import csv
import sys

INPUT_FILENAME = 'input.csv'
OUTPUT_FILENAME = 'output.csv'

def process_fdi_data(input_file, output_file):
    print(f"Початок обробки файлу: {input_file}")
    
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            header = next(reader)
            print("\nВміст вхідного файлу:")
            print(f"{' | '.join(header)}")
            
            COUNTRY_NAME_INDEX = 0
            VALUE_INDEX = 4 
            min_value_info = None 
            max_value_info = None
            
            for row in reader:
                if len(row) > VALUE_INDEX:
                    country_name = row[COUNTRY_NAME_INDEX]
                    if not country_name:
                        continue
                    raw_value = row[VALUE_INDEX].strip()                    
                    print(f"{' | '.join(row)}")
                    try:
                        if raw_value == '..' or raw_value == '':
                            fdi_value = 0.0
                        else:
                            fdi_value = float(raw_value)
                        if max_value_info is None or fdi_value > max_value_info[0]:
                            max_value_info = (fdi_value, country_name)
                        if min_value_info is None or fdi_value < min_value_info[0]:
                            min_value_info = (fdi_value, country_name)
                    except ValueError:
                        continue 
                
    except FileNotFoundError:
        print(f"\nПомилка")
        print(f"Файл '{input_file}' не знайдено.")
        print(f"Будь ласка, переконайтеся, що файл 'data.csv' перейменовано на '{input_file}' і знаходиться у тій же папці.")
        sys.exit(1)
    except Exception as e:
        print(f"\nСистемна помилка")
        print(f"Виникла несподівана помилка при читанні файлу: {e}")
        sys.exit(1)
        
    print("\nРезультати обробки")
    
    if max_value_info and min_value_info:
        max_value, max_country = max_value_info
        min_value, min_country = min_value_info
        
        print(f"Найбільше значення ПІІ: {max_value:,.2f} $ (Країна: {max_country})")
        print(f"Найменше значення ПІІ: {min_value:,.2f} $ (Країна: {min_country})")
        
        output_header = ['Результат', 'Країна', 'Значення (current US$)']
        output_data = [
            ['Найбільше значення', max_country, max_value],
            ['Найменше значення', min_country, min_value]
        ]
        
        try:
            with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(output_header)
                writer.writerows(output_data)
                
            print(f"\nРезультати успішно записано у файл: {output_file}")
            
        except Exception as e:
            print(f"\nПомилка запису")
            print(f"Виникла помилка при записі у файл '{output_file}': {e}")
            
    else:
        print("Не знайдено коректних даних для обробки.")
        

if __name__ == "__main__":
    process_fdi_data(INPUT_FILENAME, OUTPUT_FILENAME)