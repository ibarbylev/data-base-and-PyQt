"""Работа с БД через PyQt"""

import sys
from PyQt5 import QtWidgets, QtSql
from PyQt5.QtSql import QSqlQuery, QSqlDatabase

# QTableView, QTreeView, QListView

# Открытие базы данных SQLite
con1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db_path = '/home/su/Projects/GeekBrains/data-base-and-PyQt/lesson_5/examples/demo.sqlite'
con1.setDatabaseName(db_path)
print(con1.isOpen())
con1.open()
print(con1.isOpen())
print(con1.databaseName())
query = QSqlQuery()
# Добавляем нового артиста
query.exec("INSERT INTO Artist (Name) VALUES ('The New Artist')")
con1.close()

