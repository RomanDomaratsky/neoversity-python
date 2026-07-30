# Тема: Читання і запис файлів через pathlib (read_text/write_text, read_bytes/write_bytes)
# ------------------------------------------------------------------------------------------
# Path.read_text(encoding=None, errors=None) / Path.write_text(data, encoding=None, errors=None)
# errors: 'strict' (виняток), 'ignore' (пропустити), 'replace' (замінити на '?')

from pathlib import Path

# Запис і читання текстового файлу
file_path = Path("example_text.txt")
file_path.write_text("Привіт світ!", encoding="utf-8")

text = file_path.read_text(encoding="utf-8")
print(text)  # Привіт світ!


# Запис і читання бінарного файлу
bin_path = Path("example.bin")
data = b"Python is great!"
bin_path.write_bytes(data)

binary_data = bin_path.read_bytes()
print(binary_data)  # b'Python is great!'
