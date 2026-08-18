# Тема: pandas та CSV - read_csv/to_csv для реальної аналітики даних
# ------------------------------------------------------------------------
# Стандартний модуль csv добре читає файл рядок за рядком, але для
# аналітики (фільтрація, групування, обчислення) значно зручніше одразу
# отримати pandas.DataFrame з правильними типами даних.

import pandas as pd
import os
from io import StringIO

# Змодельований "брудний" CSV, типовий для реальних вивантажень:
# є пропущені значення (позначені по-різному) і дата у вигляді тексту.
raw_csv = """order_id,customer,amount,order_date,status
1,Олена Ковальчук,250.5,2024-01-15,paid
2,Іван Бондар,,2024-01-16,pending
3,Марія Гнатюк,120.75,2024-01-17,N/A
4,Петро Сидоренко,80.0,2024-01-18,paid
"""

with open("orders.csv", "w", encoding="utf-8") as f:
    f.write(raw_csv)

# --- Базове читання: усі "брудні" значення сприймаються як object/NaN без контролю ---
df_naive = pd.read_csv("orders.csv")
print(df_naive.dtypes)
print()

# --- Керіване читання: явні типи, парсинг дат, кастомні позначення пропусків ---
df = pd.read_csv(
    "orders.csv",
    dtype={"order_id": "int32", "customer": "string"},
    parse_dates=["order_date"],          # рядок дати -> datetime64
    na_values=["N/A", ""],               # різні позначення пропуску -> NaN
)
print(df.dtypes)
print(df)

# Аналітика: сумарна виручка по оплачених замовленнях
paid_total = df.loc[df["status"] == "paid", "amount"].sum()
print(f"Сума оплачених замовлень: {paid_total}")


# --- Читання ВЕЛИКИХ файлів частинами (chunksize), щоб не завантажувати все в пам'ять ---
chunk_totals = []
for chunk in pd.read_csv("orders.csv", chunksize=2, parse_dates=["order_date"]):
    chunk_totals.append(chunk["amount"].sum(skipna=True))
print(f"Суми по чанках (по 2 рядки): {chunk_totals}")


# --- Запис DataFrame назад у CSV ---
df.to_csv("orders_clean.csv", index=False, encoding="utf-8")
with open("orders_clean.csv", encoding="utf-8") as f:
    print(f.read())

for fname in ("orders.csv", "orders_clean.csv"):
    try:
        os.remove(fname)
    except OSError:
        pass

# Практичне застосування: read_csv з dtype/parse_dates/na_values - щоденний
# інструмент аналітика даних для імпорту вивантажень з CRM, платіжних
# систем чи Google Analytics; chunksize рятує, коли файл важить гігабайти і
# не влазить у оперативну пам'ять цілком.
