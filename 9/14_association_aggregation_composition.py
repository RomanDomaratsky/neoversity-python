# Тема: Асоціація, агрегація та композиція в ООП
# ------------------------------------------------------------------------
# Наслідування створює тісну залежність "є" (is-a) між класами і не завжди
# доречне. Асоціація ("має" / has-a) - клас включає інший клас як поле.
# Два підвиди асоціації:
#   Агрегація  - "частина" може існувати незалежно від "цілого".
#   Композиція - "частина" не може існувати без "цілого" (life-cycle
#                частини повністю керується цілим).


# --- Антипаттерн: неправильне використання наслідування ("Cat є Owner") ---
class OwnerWrong:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class CatWrong(OwnerWrong):  # НЕПРАВИЛЬНО: кішка - це не господар
    def __init__(self, nickname, age, name, phone):
        super().__init__(name, phone)
        self.nickname = nickname
        self.age = age

    def cat_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"


cat_wrong = CatWrong('Simon', 4, 'Boris', '+380503002010')
print(cat_wrong.info())      # Boris: +380503002010
print(cat_wrong.cat_info())  # Cat Name: Simon, Age: 4


# --- Правильно: агрегація - Cat "має" Owner, Owner існує незалежно ---
class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"


class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner  # агрегація: Cat "має" Owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"


owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)
print(cat.owner.info())   # Boris: +380503002010
print(cat.get_info())     # Cat Name: Simon, Age: 4
# owner міг би існувати і без cat - незалежний об'єкт


# --- Композиція: Project "володіє" Task, задачі не існують без проекту ---
class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")


class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))  # Task створюється всередині Project

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()


my_project = Project("Веб-розробка")

my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")

my_project.display_project_info()

my_project.remove_task("Розробка API")

my_project.display_project_info()

# Практичне застосування: агрегація - Department "має" Employee (при
# видаленні відділу співробітники не зникають, їх можна перевести кудись
# інде); композиція - Order "має" OrderLine (позиції замовлення не мають
# сенсу поза замовленням і видаляються разом з ним).
