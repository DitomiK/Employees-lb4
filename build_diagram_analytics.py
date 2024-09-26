import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

csv_file = 'employees.csv'

def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

try:
    data = pd.read_csv(csv_file, encoding='utf-8')
    print("Ok")
except FileNotFoundError:
    print("Файл CSV не знайдено.")
    exit(1)
except Exception as e:
    print(f"Помилка при відкритті файлу CSV: {e}")
    exit(1)

data['Дата народження'] = pd.to_datetime(data['Дата народження'], format='%Y-%m-%d')
data['Вік'] = data['Дата народження'].apply(calculate_age)

gender_counts = data['Стать'].value_counts()
print("Кількість співробітників за статтю:")
print(gender_counts.to_string())

plt.figure(figsize=(6, 6))
gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'pink'], labels=['Чоловіки', 'Жінки'])
plt.title('Розподіл співробітників за статтю')
plt.ylabel('')
plt.show()

age_categories = {
    'younger_18': data[data['Вік'] < 18],
    '18-45': data[(data['Вік'] >= 18) & (data['Вік'] <= 45)],
    '45-70': data[(data['Вік'] > 45) & (data['Вік'] <= 70)],
    'older_70': data[data['Вік'] > 70]
}

age_counts = {key: len(value) for key, value in age_categories.items()}
print("Кількість співробітників за віковими категоріями:")
for category, count in age_counts.items():
    print(f"{category}: {count}")

plt.figure(figsize=(8, 6))
plt.bar(age_counts.keys(), age_counts.values(), color=['blue', 'green', 'orange', 'red'])
plt.title('Кількість співробітників за віковими категоріями')
plt.xlabel('Вікові категорії')
plt.ylabel('Кількість співробітників')
plt.show()

gender_age_counts = {
    'younger_18': data[data['Вік'] < 18]['Стать'].value_counts(),
    '18-45': data[(data['Вік'] >= 18) & (data['Вік'] <= 45)]['Стать'].value_counts(),
    '45-70': data[(data['Вік'] > 45) & (data['Вік'] <= 70)]['Стать'].value_counts(),
    'older_70': data[data['Вік'] > 70]['Стать'].value_counts()
}

print("Кількість співробітників за статтю та віковими категоріями:")
for category, counts in gender_age_counts.items():
    print(f"\nКатегорія {category}:")
    print(counts.to_string())

for category, counts in gender_age_counts.items():
    plt.figure(figsize=(6, 6))
    counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, labels=['Чоловіки', 'Жінки'], colors=['lightblue', 'pink'])
    plt.title(f'Розподіл співробітників за статтю (категорія: {category})')
    plt.ylabel('')
    plt.show()
