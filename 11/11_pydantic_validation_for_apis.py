# Тема: Валідація структури даних через pydantic (API-розробка)
# ------------------------------------------------------------------------
# pydantic - бібліотека для опису схеми даних через звичайні класи з
# анотаціями типів, яка автоматично валідує вхідні дані (наприклад, тіло
# HTTP-запиту у форматі JSON) і перетворює їх у типізовані Python-об'єкти.
# Саме на pydantic побудована валідація запитів/відповідей у FastAPI.
#
# УВАГА: потрібні пакети pydantic та email-validator
# (pip install pydantic email-validator) - другий пакет потрібен саме
# для перевірки формату email через тип EmailStr.

from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import Optional


# --- Проста модель запиту на реєстрацію користувача ---
class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr
    age: int = Field(gt=0, le=120)  # вік має бути в діапазоні (0, 120]


# Валідні дані - модель створюється без помилок
valid_payload = {"name": "Олена Ковальчук", "email": "olena@example.com", "age": 28}
user = UserCreateRequest(**valid_payload)
print(user)
# name='Олена Ковальчук' email='olena@example.com' age=28
print(user.model_dump())  # перетворення назад у словник (для БД, логів)
print(user.model_dump_json())  # перетворення напряму у JSON-рядок (для відповіді API)


# --- Невалідні дані - pydantic одразу викидає детальну ValidationError ---
invalid_payload = {"name": "Іван", "email": "not-an-email", "age": -5}
try:
    UserCreateRequest(**invalid_payload)
except ValidationError as e:
    print(f"Знайдено {e.error_count()} помилок валідації:")
    for err in e.errors():
        print(f"  - поле '{err['loc'][0]}': {err['msg']}")


# --- Вкладені моделі: типова структура для API з адресою доставки ---
class Address(BaseModel):
    city: str
    street: str
    postal_code: Optional[str] = None  # необов'язкове поле


class OrderRequest(BaseModel):
    order_id: int
    customer_name: str
    total: float = Field(ge=0)  # сума не може бути від'ємною
    shipping_address: Address


order_payload = {
    "order_id": 101,
    "customer_name": "Марія Гнатюк",
    "total": 250.5,
    "shipping_address": {"city": "Одеса", "street": "вул. Дерибасівська, 1"},
}

order = OrderRequest(**order_payload)
print(order.shipping_address.city)  # Одеса - вкладена модель також типізована
print(order.model_dump())

# Спроба створити замовлення з від'ємною сумою - ValidationError
try:
    OrderRequest(**{**order_payload, "total": -10})
except ValidationError as e:
    print(f"Помилка: {e.errors()[0]['msg']}")

# Практичне застосування: у FastAPI/Django REST Framework моделі pydantic
# описують тіло запиту й відповіді API - фреймворк автоматично валідує
# вхідні дані ДО того, як вони потраплять у бізнес-логіку, повертаючи
# клієнту зрозумілу помилку 422 замість падіння сервера на некоректних
# даних.
