# Тема: Порівняння рядків без урахування регістру (lower, casefold)
# ------------------------------------------------------------------------

# lower() - приведення обох рядків до нижнього регістру перед порівнянням
string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")

# Практичне застосування: така техніка типова для входу в систему за
# логіном/email або для пошуку/фільтрації в базі даних, де користувач
# може ввести дані в довільному регістрі, а порівнювати їх треба однаково.


# casefold() - "жорсткіший" за lower(), правильно працює з мовними
# особливостями (наприклад, німецька літера "ß" -> "ss")
text = "Python Programming"
print(text.casefold())  # 'python programming' (як і lower())

german_word = 'straße'    # нижній регістр
search_word = 'STRASSE'   # верхній регістр

lower_comparison = german_word.lower() == search_word.lower()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}")        # False
print(f"Порівняння з casefold(): {casefold_comparison}")  # True
