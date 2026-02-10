import pandas as pd
from scipy.stats import mannwhitneyu

df = pd.read_csv("new-site.csv", sep="\t")
sum_A = df[df["site"] == 0]["dwell-time"].sum()
sum_B = df[df["site"] == 1]["dwell-time"].sum()
print(sum_A, sum_B)
# Вычисляем среднее время пребывания по группам
mean_A = round(df[df['site'] == 0]['dwell-time'].mean())
mean_B = round(df[df['site'] == 1]['dwell-time'].mean())

print(f"Группа А: {mean_A}")
print(f"Группа B: {mean_B}")

# Разделяем группы
group_A = df[df['site'] == 0]['dwell-time']
group_B = df[df['site'] == 1]['dwell-time']

# U-тест Манна — Уитни (двусторонний)
stat, p_value = mannwhitneyu(group_A, group_B, alternative='two-sided')

print(f"p-value = {p_value:.4f}")
print(f"Уровень значимости α = 0.05")
print(f"p-value {'< α → отвергаем H₀' if p_value < 0.05 else '> α → НЕ отвергаем H₀'}")