# Тема: Робота з директоріями через pathlib (iterdir, mkdir, rmdir, exists/is_dir/is_file)
# ------------------------------------------------------------------------------------------

from pathlib import Path

# Підготуємо демонстраційну директорію (аналог "./picture" з лекції)
demo_dir = Path("picture_demo")
demo_dir.mkdir(exist_ok=True)
(demo_dir / "bot-icon.png").write_text("demo text")
(demo_dir / "mongodb.jpg").write_text("demo text")
(demo_dir / "Logo").mkdir(exist_ok=True)

# iterdir() - перелік усіх файлів і піддиректорій у директорії
for path in demo_dir.iterdir():
    print(path)


# mkdir() - створення нової директорії
# Практичне застосування: скрипти встановлення/деплою часто мають підготувати
# структуру директорій проєкту (наприклад, logs/, config/, data/) - parents=True
# створює всі відсутні батьківські директорії, а exist_ok=True робить операцію
# безпечною для повторного запуску (не впаде, якщо директорія вже є).
new_dir = Path("my_directory/new_folder")
new_dir.mkdir(parents=True, exist_ok=True)
print(new_dir.exists())  # True

# rmdir() - видалення директорії (директорія має бути ПОРОЖНЬОЮ)
new_dir.rmdir()
print(new_dir.exists())  # False


# Перевірки existence/is_dir/is_file
path = demo_dir
if path.exists():
    print(f"{path} існує")
if path.is_dir():
    print(f"{path} є директорією")
if (demo_dir / "bot-icon.png").is_file():
    print(f"{demo_dir / 'bot-icon.png'} є файлом")
