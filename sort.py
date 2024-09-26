from datetime import datetime
import pandas as pd

csv_file = 'employees.csv'
xlsx_file = 'employees_categorized.xlsx'

def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

try:
    data = pd.read_csv(csv_file, encoding='utf-8')
except FileNotFoundError:
    print("Файл CSV не знайдено.")
    exit(1)
except Exception as e:
    print(f"ППомилка при відкритті файлу CSV: {e}")
    exit(1)


data['Дата народження'] = pd.to_datetime(data['Дата народження'], format='%Y-%m-%d')
data['Вік'] = data['Дата народження'].apply(calculate_age)

try:
    with pd.ExcelWriter(xlsx_file, engine='openpyxl') as writer:
        data.to_excel(writer, sheet_name='all', index=False, columns=['Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження', 'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'])

        younger_18 = data[data['Вік'] < 18]
        younger_18.to_excel(writer, sheet_name='younger_18', index=False, columns=['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік'])

        between_18_45 = data[(data['Вік'] >= 18) & (data['Вік'] <= 45)]
        between_18_45.to_excel(writer, sheet_name='18-45', index=False, columns=['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік'])

        between_45_70 = data[(data['Вік'] > 45) & (data['Вік'] <= 70)]
        between_45_70.to_excel(writer, sheet_name='45-70', index=False, columns=['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік'])

        older_70 = data[data['Вік'] > 70]
        older_70.to_excel(writer, sheet_name='older_70', index=False, columns=['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік'])

    print("Ok")
except Exception as e:
    print(f"Неможливо створити XLSX файл: {e}")
