# Тема: Той самий приклад через "from utility import *"
# ------------------------------------------------------------------------
# Працює тільки завдяки __all__ = ['nice_function', 'not_bad'] в __init__.py -
# саме цей список визначає, що потрапить у поточний простір імен.

from utility import *

nice_function()
print(not_bad("Test string"))
