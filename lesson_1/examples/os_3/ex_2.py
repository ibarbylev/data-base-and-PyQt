"""Функции модуля os"""

import os
# когда нужно переименовать файл или папку
# os.rename("old_dir", "new_dir")

# Метод os.startfile() позволяет нам «запустить»
# файл в привязанной к нему программе.
import platform

if platform.system() == 'Windows':
    os.startfile("Сложность алгоритмов.png")
# else:
#     file_path = os.path.join(os.getcwd(), 'Сложность алгоритмов.png')
#     os.system(f"eog '{file_path}'")

PATH = "dirs"

"""
\dirs
\dirs\d1\f1.txt
\dirs\d2\f2.txt
\dirs\d3\f3.txt
"""

# root - очередной внутренний путь к папке включая текущую
# dirs - список папок в каждом пути root
# files - список файлов в каждом пути root
for root, dirs, files in os.walk(PATH):
    print('-' * 50)
    print(root)
    print(dirs)
    print(files)

print()
print('=' * 50)
for root, dirs, files in os.walk(PATH):
    print(root, dirs, files)
