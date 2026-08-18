# Тема: Серіалізація JSON - json.dumps / json.loads
# ------------------------------------------------------------------------
# JSON (JavaScript Object Notation) - текстовий, мовонезалежний формат
# обміну даними. dumps()/loads() працюють з РЯДКАМИ (на відміну від
# dump()/load(), що працюють з файлами).
#
# Правила кодування Python -> JSON:
#   dict            -> object {}
#   list, tuple     -> array []      (JSON НЕ розрізняє список і кортеж!)
#   str             -> string
#   int, float      -> number
#   True / False    -> true / false
#   None            -> null

import json

some_data = {
    "key": "value",
    2: [1, 2, 3],
    "my_tuple": (5, 6),
    "my_dict": {"key": "value"},
}

json_string = json.dumps(some_data)
print(json_string)
# {"key": "value", "2": [1, 2, 3], "my_tuple": [5, 6], "my_dict": {"key": "value"}}

unpacked_some_data = json.loads(json_string)
print(unpacked_some_data)
# {'key': 'value', '2': [1, 2, 3], 'my_tuple': [5, 6], 'my_dict': {'key': 'value'}}

# УВАГА: unpacked_some_data НЕ ідентичний some_data:
#  - ключ 2 (int) перетворився на рядок "2" -> '2'
#  - кортеж (5, 6) перетворився на список [5, 6]
print(unpacked_some_data == some_data)  # False

# Практичне застосування: dumps()/loads() використовують для обміну даними
# через мережу - наприклад, підготовка тіла HTTP-запиту (json.dumps(payload))
# або розбір відповіді REST API (json.loads(response.text)).
