# Тема: Формат Parquet - колонкове зберігання для аналітики великих даних
# ------------------------------------------------------------------------
# Parquet - бінарний, КОЛОНКОВИЙ формат зберігання табличних даних
# (на відміну від CSV, який зберігає дані ПОРЯДКОВО, рядок за рядком).
# Переваги перед CSV:
#   - зберігає типи даних (int, float, datetime) - не треба перевизначати
#     dtype/parse_dates при кожному читанні, як у CSV;
#   - стискає дані значно ефективніше (особливо повторювані значення);
#   - читання лише потрібних колонок без парсингу всього файлу -
#     критично для аналітики з мільйонами рядків.
# Вимагає пакет pyarrow (pip install pyarrow), який pandas використовує
# "під капотом" для читання/запису Parquet.

import pandas as pd
import numpy as np
import os

# Створимо відносно великий тестовий датасет (10 000 рядків)
rng = np.random.default_rng(seed=42)
n = 10_000
df = pd.DataFrame({
    "order_id": range(1, n + 1),
    "customer": [f"Клієнт {i % 500}" for i in range(n)],
    "amount": rng.uniform(10, 1000, size=n).round(2),
    "order_date": pd.date_range("2024-01-01", periods=n, freq="h"),
    "status": rng.choice(["paid", "pending", "canceled"], size=n),
})

# Зберігаємо той самий датасет в обох форматах
df.to_csv("orders.csv", index=False)
df.to_parquet("orders.parquet", index=False)  # потребує pyarrow

csv_size = os.path.getsize("orders.csv")
parquet_size = os.path.getsize("orders.parquet")
print(f"Розмір CSV:     {csv_size:,} байт")
print(f"Розмір Parquet: {parquet_size:,} байт")
print(f"Parquet менший у {csv_size / parquet_size:.1f} рази")


# --- Типи даних: CSV втрачає типи, Parquet - зберігає ---
df_from_csv = pd.read_csv("orders.csv")
df_from_parquet = pd.read_parquet("orders.parquet")

print("\nТипи після читання з CSV (дата стала звичайним рядком):")
print(df_from_csv.dtypes["order_date"])  # object

print("\nТипи після читання з Parquet (дата залишилась datetime):")
print(df_from_parquet.dtypes["order_date"])  # datetime64[ns]


# --- Читання лише потрібних колонок - Parquet дозволяє не парсити зайве ---
partial = pd.read_parquet("orders.parquet", columns=["order_id", "amount"])
print(f"\nЗчитано лише колонки: {partial.columns.tolist()}")


for fname in ("orders.csv", "orders.parquet"):
    try:
        os.remove(fname)
    except OSError:
        pass

# Практичне застосування: Parquet - стандарт де-факто для аналітичних
# сховищ даних (data lakes) та інструментів на кшталт Spark, Hive, Amazon
# Athena, Google BigQuery - обирають його замість CSV, коли датасети важать
# гігабайти чи терабайти і важлива швидкість читання та економія місця.
