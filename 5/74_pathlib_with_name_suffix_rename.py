# Тема: Маніпуляція компонентами шляху - with_name, with_suffix, rename
# ------------------------------------------------------------------------
# with_name()/with_suffix() створюють НОВИЙ об'єкт Path (не змінюють файл на диску).
# rename() - реально перейменовує файл на диску.

from pathlib import Path
import os

os.makedirs('documents', exist_ok=True)

# with_name() - заміна імені файлу в шляху
original_path = Path("documents/example.txt")
new_path = original_path.with_name("report.txt")
print(new_path)  # documents/report.txt

# with_suffix() - заміна/додавання розширення файлу
new_path_md = original_path.with_suffix(".md")
print(new_path_md)  # documents/example.md

# with_name/with_suffix НЕ змінюють оригінал - лише повертають новий Path
print(original_path)  # documents/example.txt (без змін)
print(new_path)        # documents/report.txt (новий об'єкт)

# rename() - фізична зміна імені файлу на диску
original_path.write_text("demo text")  # створюємо файл для прикладу
original_path.rename(new_path)
print(new_path.exists())        # True
print(original_path.exists())   # False (файл перейменовано)
