"""БД и курсор как итератор"""

# Подключение библиотеки, соответствующей типу требуемой базы данных
import os
import sqlite3

DB_OBJ = os.path.join(os.path.dirname(__file__), "demo.sqlite")

# Создание соединения с базой данных
# В данном случае это файл базы
CONN = sqlite3.connect(DB_OBJ)
# CONN = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

# Создаем курсор — это специальный объект,
# который делает запросы и получает их результаты
CURSOR = CONN.cursor()

# ---------------------------Курсор как итератор-------------------------- #
# Использование курсора как итератора
FETCH = CURSOR.execute('SELECT Name FROM Artist ORDER BY Name LIMIT 3')
print(FETCH)
print(list(FETCH))
print('=' * 50)

# Извлечеие элементов из CURSOR с помощью цикла for
for row in CURSOR.execute('SELECT Name FROM Artist ORDER BY Name LIMIT 3'):
    print(row)

# Полученный результат:
'''
('A Cor Do Som',)
('AC/DC',)
('Aaron Copland & London Symphony Orchestra',)
'''
