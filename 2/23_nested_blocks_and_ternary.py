# Тема: Блоки інструкцій (відступи), вкладеність та тернарні оператори
# ----------------------------------------------------------------------------


def indentation_demo():
    # Виділення блоку інструкцій відступом (рекомендовано 4 пробіли)
    x = int(input("X: "))
    y = int(input("Y: "))
    if x == 0:
        print("X can`t be equal to zero")
        x = int(input("X: "))
    result = y / x
    print(result)


# Визначення чверті координатної площини (вкладені if)
def quadrant(x, y):
    if x >= 0:
        if y >= 0:  # x > 0, y > 0
            print("Перша чверть")
        else:  # x > 0, y < 0
            print("Четверта чверть")
    else:
        if y >= 0:  # x < 0, y > 0
            print("Друга чверть")
        else:  # x < 0, y < 0
            print("Третя чверть")


quadrant(3, 5)    # Перша чверть
quadrant(3, -5)   # Четверта чверть
quadrant(-3, 5)   # Друга чверть
quadrant(-3, -5)  # Третя чверть


# --- Тернарні оператори ---

# Скорочена форма if-else в одному рядку
is_nice = True
state = "nice" if is_nice else "not nice"
print(state)  # nice

# Той самий результат через звичайний if-else (для порівняння)
is_nice = True
if is_nice:
    state = "nice"
else:
    state = "not nice"
print(state)  # nice

# Тернарний вираз через оператор or - швидке значення за замовчуванням
some_data = None
msg = some_data or "Не було повернено даних"
print(msg)  # Не було повернено даних

# Той самий результат через звичайний if-else (для порівняння)
some_data = None
if some_data:
    msg = some_data
else:
    msg = "Не було повернено даних"
print(msg)  # Не було повернено даних
