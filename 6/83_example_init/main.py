# Тема: Зручний імпорт завдяки __init__.py з реекспортом функцій
# ------------------------------------------------------------------------
# Без __init__.py довелося б писати так (незручно, треба знати внутрішню
# структуру пакета):
#   import utility
#   utility.useful.functions.nice_function()
#   utility.dummy.functions.not_bad("Test string")
#
# Завдяки реекспорту в utility/__init__.py можна писати простіше:

from utility import nice_function, not_bad

nice_function()
print(not_bad("Test string"))          # Test string (без "not bad" - не змінюється)
print(not_bad("This is not bad at all"))  # This is good at all
