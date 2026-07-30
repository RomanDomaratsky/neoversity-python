# Тема: pathlib + shutil (копіювання/переміщення), stat(), unlink()
# ------------------------------------------------------------------------

import shutil
import time
from pathlib import Path

# pathlib добре інтегрується з shutil для копіювання й переміщення файлів
Path("source_dir").mkdir(exist_ok=True)
source = Path("source_dir/file.txt")
source.write_text("file content", encoding="utf-8")

destination_dir = Path("destination_dir")
destination_dir.mkdir(exist_ok=True)
destination = destination_dir / "file.txt"

# shutil.copy() копіює тільки вміст; shutil.copy2() копіює і метадані
shutil.copy(source, destination)
print(destination.exists())  # True

# shutil.move() переміщує файл або директорію
moved_destination = destination_dir / "file_moved.txt"
shutil.move(destination, moved_destination)
print(moved_destination.exists())  # True


# stat() - інформація про файл: розмір, час створення/модифікації
file_path = moved_destination
size = file_path.stat().st_size
print(f"Розмір файлу: {size} байтів")

creation_time = file_path.stat().st_birthtime
modification_time = file_path.stat().st_mtime
print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")


# unlink() - видалення файлу
# Практичне застосування: missing_ok=True робить прибирання тимчасових файлів
# у скриптах ідемпотентним (безпечним для повторного запуску) - не потрібно
# окремо перевіряти exists(), скрипт не впаде, навіть якщо файл вже видалено.
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')

# Видалення без попередньої перевірки - винятку не буде, навіть якщо файлу немає
file_path.unlink(missing_ok=True)
