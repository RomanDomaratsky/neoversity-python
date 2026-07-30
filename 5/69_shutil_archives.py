# Тема: Створення та розпаковка архівів (модуль shutil)
# ------------------------------------------------------------------------
# shutil.make_archive(base_name, format, root_dir=None, base_dir=None)
# shutil.unpack_archive(filename, extract_dir=None, format=None)

import shutil
import os

# Підготуємо демонстраційну директорію з файлом (аналог "my_folder" з лекції)
os.makedirs('my_folder', exist_ok=True)
with open('my_folder/readme.txt', 'w', encoding='utf-8') as f:
    f.write('Демонстраційний файл для архівації')

# Створення ZIP-архіву з вмісту директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='my_folder')
print("ZIP-архів створено: example.zip")

# Створення TAR.GZ-архіву (стиснення GZIP)
shutil.make_archive('example', 'gztar', root_dir='my_folder')
print("TAR.GZ-архів створено: example.tar.gz")

# Практичне застосування: автоматизація резервного копіювання (backup)
# проєкту чи бази даних за розкладом, пакування вихідного коду й ресурсів
# перед публікацією релізу, чи стиснення логів перед відправкою на сервер.

# Розпакування ZIP-архіву у вказану директорію
shutil.unpack_archive('example.zip', 'destination_folder')
print("Архів розпаковано у destination_folder")
print(os.listdir('destination_folder'))  # ['readme.txt']
