# Тема: Той самий приклад, але з прямим імпортом функції з підмодуля пакета
# ------------------------------------------------------------------------------

from calculations.salary_calculations import add_bonus

salary = 1000
bonus = 15
salary_with_bonus = add_bonus(salary, bonus)
print(salary_with_bonus)  # 1015
