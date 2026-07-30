# Тема: Основи модуля pathlib - PurePath та Path
# ------------------------------------------------------------------------
# PurePath - маніпуляція шляхами БЕЗ доступу до файлової системи.
# Path (наслідує PurePath) - додає операції з реальними файлами/директоріями.

from pathlib import PurePath, Path

# PurePath - розбір шляху на складові
p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)      # simple.jpg
print("Suffix:", p.suffix)  # .jpg
print("Parent:", p.parent)  # /usr/bin


# Path - робота з реальним файлом (створення, запис, читання, перевірка)
p = Path("example.txt")
p.write_text("Hello, world!")
print(p.read_text())      # Hello, world!
print("Exists:", p.exists())  # True
