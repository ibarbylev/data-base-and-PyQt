"""Функции модуля os"""

import os

# Функция basename вернет название файла пути
# Это очень полезная функция, особенно в тех случаях,
# когда нужно использовать имя файла для наименования того
# или иного связанного с работой файла, например лог-файл.
# Такая ситуация возникает часто при работе с файлами данных.
CUR_F = os.path.basename(
    "/home/su/Projects/GeekBrains/data-base-and-PyQt/lesson_1/examples/os_3/ex_3.py")
print(CUR_F)

# Функция dirname возвращает только часть каталога пути.
# В данном примере мы просто возвращаем путь к каталогу.
# Это также полезно, когда вам нужно сохранить другие файлы рядом с тем,
# который вы обрабатываете в данный момент. Как и в случае с лог-файлом, упомянутым выше.
CUR_D_PATH = os.path.dirname(
    "/home/su/Projects/GeekBrains/data-base-and-PyQt/lesson_1/examples/os_3/ex_3.py")
print(CUR_D_PATH)

# Функция exists говорит нам, существует ли файл, или нет.
print('is exists: ', os.path.exists(
    "/home/su/Projects/GeekBrains/data-base-and-PyQt/lesson_1/examples/ipaddress_2"))

# Функция isfile говорит нам, явдяется ли объект файлом
print('isfile: ', os.path.isfile(
    "/home/su/Projects/GeekBrains/data-base-and-PyQt/lesson_1/examples/os_3/ex_3.py"))

# Функция isdir говорит нам, явдяется ли объект файлом
print('isdir: ', os.path.isdir(
    "/home/su/Projects/GeekBrains/data-base-and-PyQt/lesson_1/examples/os_3/ex_3.py"))

# Метод join позволяет вам совместить несколько путей при помощи присвоенного разделителя.
# К примеру, в Windows, в роли разделителя выступает бэкслэш (косая черта, указывающая назад),
# однако в Linux функция разделителя присвоена косой черте, указывающей вперед (forward slash).
print(os.path.join(
    "/home/su/Projects/GeekBrains/data-base-and-PyQt/lesson_1/examples/os_3",
    "3.py"))

# Метод split разъединяет путь на tuple, который содержит и файл и каталог.
print(os.path.split(
    "/home/su/Projects/GeekBrains/data-base-and-PyQt/lesson_1/examples/os_3/ex_3.py"))

# Метод listdir выдаёт список файлов и папок ('.' - означает текущую директорию)
DIR_STRUCT = os.listdir('.')
print('current dir: ', os.getcwd())
print(DIR_STRUCT)
