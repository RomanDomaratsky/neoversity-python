# Тема: collections.UserList - модифіковані списки
# ------------------------------------------------------------------------
# UserList дозволяє створювати власні версії списків з додатковою
# поведінкою, зберігаючи всю звичну поведінку list (append, indexing тощо).

from collections import UserList


class MyList(UserList):
    # Метод для додавання елемента, якщо він ще не існує
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)


my_list = MyList([1, 2, 3])
print("Оригінальний список:", my_list)  # Оригінальний список: [1, 2, 3]

my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
print("Оновлений список:", my_list)  # Оновлений список: [1, 2, 3, 4]


# --- Практичний приклад: список, що вміє підсумовувати свій вміст ---
class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))


countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum())  # 15

# Практичне застосування: такий підхід корисний для колекцій з бізнес-
# логікою "поверх" списку - наприклад, список товарів у кошику з методом
# total_price(), список подій із фільтрацією за датою тощо, без ризиків
# прямого наслідування від list.
