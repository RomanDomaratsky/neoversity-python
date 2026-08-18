# Тема: pandas та JSON - json_normalize, read_json, to_json
# ------------------------------------------------------------------------
# Реальні відповіді REST API майже завжди мають ВКЛАДЕНУ структуру JSON
# (об'єкт в об'єкті, списки об'єктів тощо). pandas.json_normalize()
# перетворює таку вкладену структуру у плоску таблицю (DataFrame),
# автоматично "розгортаючи" вкладені поля через крапку в імені колонки.

import pandas as pd
import json
from io import StringIO

# Типова відповідь API замовлень з вкладеною інформацією про клієнта
api_response = [
    {
        "order_id": 101,
        "total": 250.50,
        "customer": {"name": "Олена Ковальчук", "city": "Київ"},
        "items": ["ноутбук", "мишка"],
    },
    {
        "order_id": 102,
        "total": 45.00,
        "customer": {"name": "Іван Бондар", "city": "Львів"},
        "items": ["книга"],
    },
    {
        "order_id": 103,
        "total": 120.75,
        "customer": {"name": "Марія Гнатюк", "city": "Одеса"},
        "items": ["навушники", "чохол"],
    },
]

# json_normalize "розплющує" вкладені словники - customer.name, customer.city
df = pd.json_normalize(api_response)
print(df)
print(df.columns.tolist())
# ['order_id', 'total', 'customer.name', 'customer.city', 'items']
# (точний порядок колонок залежить від версії pandas, суть незмінна)

# Аналітика поверх сплющеної таблиці - те, заради чого це робиться
total_by_city = df.groupby("customer.city")["total"].sum()
print(total_by_city)


# --- pd.read_json / pd.to_json: пряма робота з JSON файлами/рядками ---
json_string = json.dumps(api_response)

# read_json очікує файлоподібний обʼєкт для рядкового JSON - обгортаємо в StringIO
df_from_json = pd.read_json(StringIO(json_string))  # без розгортання вкладеності
print(df_from_json["customer"].iloc[0])  # {'name': 'Олена Ковальчук', 'city': 'Київ'}
# customer тут - це просто словник у клітинці, для аналітики його все одно
# треба буде пропустити через json_normalize

# Збереження DataFrame назад у JSON
json_output = df[["order_id", "total"]].to_json(orient="records", force_ascii=False)
print(json_output)
# [{"order_id":101,"total":250.5},{"order_id":102,"total":45.0},{"order_id":103,"total":120.75}]

# Практичне застосування: json_normalize - щоденний інструмент аналітика
# даних при роботі з відповідями REST API (наприклад, вивантаження з
# Google Analytics, Stripe, CRM-систем), де дані завжди приходять
# вкладеними списками словників, а не готовими плоскими таблицями.
