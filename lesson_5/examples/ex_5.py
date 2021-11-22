"""Работа с БД через PyQt"""

import sys
from PyQt5 import QtWidgets, QtSql
from PyQt5.QtSql import QSqlQuery, QSqlDatabase

# QTableView, QTreeView, QListView

# Открытие базы данных SQLite
con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db_path = '/home/su/Projects/GeekBrains/data-base-and-PyQt/lesson_3/examples/demo.sqlite'
con1.setDatabaseName(db_path)
print(con1.isOpen())
con1.open()
print(con1.isOpen())
print(con1.databaseName())
query = QSqlQuery()
# !!!!   добавить пример от сюда: https://realpython.com/python-pyqt-database/ !!!!
query.exec("SELECT Name FROM Artist ORDER BY Name LIMIT 3")  # заменить SELECT на INSERT!!!
con1.close()

# Открытие базы данных MySQL
# con2 = QtSql.QSqlDatabase.addDatabase('QMYSQL')
# con2.setHostName('localhost')
# con2.setDatabaseName('TestDB')
# con2.setUserName('Mario')
# con2.setPassword('karabuka')
# con2.open()
# con2.close()
