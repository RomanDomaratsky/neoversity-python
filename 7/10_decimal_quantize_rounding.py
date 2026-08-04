# Тема: Decimal.quantize() та режими округлення
# ------------------------------------------------------------------------
# quantize() округлює число за ШАБЛОНОМ (наприклад, Decimal('0.00') означає
# "залиш рівно 2 знаки після коми").
# Практичне застосування: quantize() - стандартний спосіб коректно округлити
# грошові суми до копійок/центів у фінансових розрахунках і звітах.

from decimal import Decimal, ROUND_DOWN

number = Decimal('3.14159')
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
print(rounded_number)  # 3.14


# --- Основні режими округлення ---
import decimal

number = Decimal("1.45")

# За замовчуванням - ROUND_HALF_EVEN ("банківське округлення": нічия
# округляється до найближчого ПАРНОГО числа - зменшує сумарну похибку)
print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))
# 1.4

# ROUND_HALF_UP - при нічиї округлює ВГОРУ
print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))
# 1.5

# ROUND_FLOOR - завжди до найближчого МЕНШОГО значення
print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))
# 1.4

# ROUND_CEILING - завжди до найближчого БІЛЬШОГО значення
print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))
# 1.5

# Округлення до трьох знаків після коми (шаблон визначає кількість знаків)
print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000")))
# 3.142

# Інші режими для довідки:
# ROUND_UP        - округлення ВІД нуля (додатні - вгору, від'ємні - вниз за модулем)
# ROUND_DOWN      - округлення ДО нуля (додатні - вниз, від'ємні - вгору за модулем)
# ROUND_HALF_DOWN - при нічиї округлює ВНИЗ (на відміну від HALF_UP)
