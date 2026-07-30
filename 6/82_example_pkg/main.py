# Тема: Пакети - директорія calculations/ як пакет з модулем salary_calculations
# ------------------------------------------------------------------------------
# Структура:
#   example_pkg/
#     calculations/
#       salary_calculations.py
#     main.py
from calculations import salary_calculations

salary = 1000
bonus = 15
salary_with_bonus = salary_calculations.add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015
