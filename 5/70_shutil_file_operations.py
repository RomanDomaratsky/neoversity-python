# Тема: Високорівневі файлові операції модуля shutil
# ------------------------------------------------------------------------
# shutil.copy(src, dst)      - копіює файл
# shutil.copytree(src, dst)  - рекурсивно копіює директорію
# shutil.move(src, dst)      - переміщує файл або директорію
# shutil.rmtree(path)        - рекурсивно видаляє директорію
# shutil.disk_usage(path)    - статистика використання диска

import shutil
import os

# --- Ілюстративний приклад з лекції (шляхи умовні, для довідки) ---
# source_file = '/path/to/source/file.txt'
# destination_dir = '/path/to/destination'
# shutil.copy(source_file, destination_dir)
#
# source_dir = '/path/to/source/directory'
# destination_dir = '/path/to/destination/directory'
# shutil.copytree(source_dir, destination_dir)


# --- Той самий приклад на реальних тимчасових файлах, щоб побачити результат ---
os.makedirs('source', exist_ok=True)
with open('source/file.txt', 'w', encoding='utf-8') as f:
    f.write('дані для копіювання')
os.makedirs('destination', exist_ok=True)

# Копіюємо файл (тільки вміст, без метаданих)
shutil.copy('source/file.txt', 'destination')
print(os.listdir('destination'))  # ['file.txt']

# Копіюємо всю директорію рекурсивно
shutil.copytree('source', 'destination_dir_copy')
print(os.listdir('destination_dir_copy'))  # ['file.txt']

# Переміщуємо файл в іншу директорію
shutil.move('destination/file.txt', 'destination_dir_copy/moved_file.txt')
print(os.listdir('destination_dir_copy'))  # ['file.txt', 'moved_file.txt']

# Статистика використання диска для поточної директорії
usage = shutil.disk_usage('.')
print(f"Всього: {usage.total}, використано: {usage.used}, вільно: {usage.free}")

# Рекурсивне видалення директорії (обережно - незворотна операція!)
shutil.rmtree('destination_dir_copy')
print(os.path.exists('destination_dir_copy'))  # False
