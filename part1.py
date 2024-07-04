import pandas as pd
import numpy as np


data = {
    'Имя': ['Анна', 'Мария', 'Виктор', 'Галина', 'Дмитрий', 'Елена', 'Егор', 'Зоя', 'Антон', 'Екатерина'],
    'Математика': [85, 78, 92, 88, 76, 95, 89, 74, 91, 84],
    'Литература': [82, 79, 85, 90, 78, 84, 87, 75, 89, 81],
    'Химия': [88, 76, 92, 85, 79, 90, 84, 77, 91, 80],
    'Биология': [90, 80, 88, 92, 77, 85, 89, 79, 87, 82],
    'История': [85, 77, 90, 88, 76, 92, 84, 78, 89, 83]
}

df = pd.DataFrame(data)

print("Первые несколько строк DataFrame:")
print(df.head(), "\n")

mean_scores = df.mean(numeric_only=True)
print("Средняя оценка по каждому предмету:")
print(mean_scores, "\n")

median_scores = df.median(numeric_only=True)
print("Медианная оценка по каждому предмету:")
print(median_scores, "\n")

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"Q1 для оценок по математике: {Q1_math}")
print(f"Q3 для оценок по математике: {Q3_math}\n")

IQR_math = Q3_math - Q1_math
print(f"IQR для оценок по математике: {IQR_math}\n")

std_dev = df.std(numeric_only=True)
print("Стандартное отклонение по каждому предмету:")
print(std_dev)
