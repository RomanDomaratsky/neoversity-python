# Тема: Створення та об'єднання шляхів у pathlib
# ------------------------------------------------------------------------
# Path автоматично адаптується до синтаксису шляхів конкретної ОС.

from pathlib import Path

# Створення шляхів (в Unix - '/', у Windows - '\', pathlib абстрагує це)
path_unix = Path("/usr/bin/python3")
path_windows = Path("C:/Users/Username/Documents/file.txt")
print(path_unix)
print(path_windows)

# Об'єднання шляхів за допомогою оператора / (замість ручної конкатенації рядків)
base_path = Path("/usr/bin")
full_path = base_path / "subdir" / "script.py"
print(full_path)  # /usr/bin/subdir/script.py (або з \ у Windows)
