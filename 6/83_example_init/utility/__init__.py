# Файл __init__.py виконується Python автоматично при ПЕРШОМУ імпорті пакета.
# Тут ми "піднімаємо" функції з глибоко вкладених підмодулів на верхній
# рівень пакета utility, щоб користувачу не потрібно було знати про
# внутрішню структуру (utility/useful/functions.py, utility/dummy/functions.py).

from utility.useful.functions import nice_function
from utility.dummy.functions import not_bad

# __all__ визначає, що саме імпортується при "from utility import *"
__all__ = ['nice_function', 'not_bad']
