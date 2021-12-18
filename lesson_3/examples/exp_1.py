"""БД и запросы на выборку"""

# Подключение библиотеки, соответствующей типу базы данных
import os
import sqlite3

db_full_path = os.path.join(os.path.dirname(__file__), "demo.sqlite")

# Создание соединения с базой данных
# В данном случае это файл базы
connect = sqlite3.connect(db_full_path)
# connect = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

# Создаем курсор — это специальный объект,
# который делает запросы и получает их результаты
cursor = connect.cursor()

# ---------------------------Запрос на выборку----------------------------- #

cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")

# метод .fetchall() позволяет получить все данные сразу в виде списка
# в котором каждая строка таблицы Artist представлена отдельным тюплом
results = cursor.fetchall()  # [('A Aagrh!',), ('A Aagrh!',), ('A Aagrh!',)]
print(results)

# повторное обращение к объекту cursor вернёт пустой список,
# т.к. результаты запроса уже обработаны
results_2 = cursor.fetchall()  # []
print(results_2)


# Таким образом, cursor обладает свойствами итератора
# и с помощью метода .fetchone() мы можем извлекать данные построчно
cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

"""
('A Cor Do Som',)
('AC/DC',)
('Aaron Copland & London Symphony Orchestra',)
None

---------------------------
Как видим, последний запрос вернул None, означающий, 
что все данные из объекта cursor уже извлечены
"""


