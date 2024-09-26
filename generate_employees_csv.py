import csv
from faker import Faker
import random

fake = Faker('uk_UA')
total_records = 2000
male_ratio = 0.6
female_ratio = 0.4
male_count = int(total_records * male_ratio)
female_count = total_records - male_count

def generate_male_record():
    return {
        'Прізвище': fake.last_name_male(),
        'Ім’я': fake.first_name_male(),
        'По батькові': fake.middle_name_male(),
        'Стать': 'Чоловіча',
        'Дата народження': fake.date_of_birth(minimum_age=16, maximum_age=85).strftime('%Y-%m-%d'),
        'Посада': fake.job(),
        'Місто проживання': fake.city(),
        'Адреса проживання': fake.address(),
        'Телефон': fake.phone_number(),
        'Email': fake.email()
    }

def generate_female_record():
    return {
        'Прізвище': fake.last_name_female(),
        'Ім’я': fake.first_name_female(),
        'По батькові': fake.middle_name_female(),
        'Стать': 'Жіноча',
        'Дата народження': fake.date_of_birth(minimum_age=16, maximum_age=85).strftime('%Y-%m-%d'),
        'Посада': fake.job(),
        'Місто проживання': fake.city(),
        'Адреса проживання': fake.address(),
        'Телефон': fake.phone_number(),
        'Email': fake.email()
    }

records = []
for _ in range(male_count):
    records.append(generate_male_record())

for _ in range(female_count):
    records.append(generate_female_record())

random.shuffle(records)

with open('employees.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

print("Ok")
