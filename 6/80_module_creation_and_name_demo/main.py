# Тема: Використання власного модуля mymodule.py + функція dir()
# ------------------------------------------------------------------------

import mymodule

print(mymodule.say_hello("World"))  # Hello, World! (доступ через ім'я модуля)

# Вибірковий імпорт конкретної функції
from mymodule import say_hello

print(say_hello("World"))

# Імпорт з псевдонімом (alias)
from mymodule import say_hello as greeting

print(greeting("World"))

# dir() без аргументів - список імен у ПОТОЧНІЙ області видимості (цього файлу).
# Тут буде видно "mymodule" (бо є import mymodule), "say_hello" та "greeting" -
# усі імена, які ми явно імпортували чи створили в цьому файлі.
print(dir())

# dir(mymodule) - список усього, що визначено В САМОМУ модулі mymodule
print(dir(mymodule))
