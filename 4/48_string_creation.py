# Тема: Варіанти створення рядків
# ------------------------------------

# Одинарні та подвійні лапки рівнозначні
this_is_string = "Hi there!"
the_same_string = 'Hi there!'
print(this_is_string == the_same_string)  # True

# Потрійні лапки - для багаторядкових рядків
text = """This is first line
And second line
Last third line"""
print(text)

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''
print(song)

# Довгий рядок без перенесень, розбитий на частини за допомогою \
one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."
print(one_line_text)

# Неявна конкатенація: рядки поруч без + автоматично об'єднуються
print(("spam " "eggs") == "spam eggs")  # True

# Той самий довгий рядок через неявну конкатенацію (без \)
one_line_text = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")
print(one_line_text)

# Практичне застосування: побудова довгих SQL-запитів частинами -
# зручно редагувати кожну частину запиту окремо, і легко додавати/
# видаляти умови без "склеювання" одного величезного рядка.
query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")
print(query)
