# Тема: Відносні й абсолютні шляхи в pathlib
# ------------------------------------------------------------------------
# Абсолютний шлях - повний шлях від кореня файлової системи.
# Відносний шлях - шлях відносно поточного робочого каталогу.

from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt")
absolute_path = relative_path.absolute()
print(absolute_path)  # залежить від поточного робочого каталогу

# relative_to() - зворотна операція: отримати відносний шлях щодо директорії
current_working_directory = Path.cwd()
back_to_relative = absolute_path.relative_to(current_working_directory)
print(back_to_relative)  # documents/example.txt
