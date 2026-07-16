# Тема: Змінність об'єктів (mutable/immutable) при передачі у функції
# ------------------------------------------------------------------------

# Незмінний тип (str) - зміна всередині функції НЕ впливає на оригінал
def modify_string(original: str) -> str:
    original = "змінено"
    return original


str_var = "оригінал"
print(modify_string(str_var))  # змінено
print(str_var)                 # оригінал (без змін)


# Змінний тип (list) - зміна всередині функції ВПЛИВАЄ на оригінал
def modify_list(lst: list) -> None:
    lst.append(4)


my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4]


# Щоб уникнути зміни оригіналу - використовуйте copy()
def modify_list_safe(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)


my_list = [1, 2, 3]
modify_list_safe(my_list)
print(my_list)  # [1, 2, 3] (без змін)
