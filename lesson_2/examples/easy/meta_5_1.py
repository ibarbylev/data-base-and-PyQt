"""
Способы создания Метаклассов с помощью встроенной функции type
type(<name>, <bases>, <dct>),
где
<name> - имя нового класса (станет __name__-атрибутом нового класса).
<bases> - тюпл из базовых классов, которые наследует новый класс
          (станет __bases__-атрибутом нового класса).
<dct> - словарь пространства имён, содержащий определения для тела класса
         (станет __dict__-атрибутом нового класса).
"""
from pprint import pprint

MyMeta = type('MyMeta', (list,), dict(x=5, y=6))

print('type(MyMeta):     ', type(MyMeta))
print('MyMeta.__name__:  ', MyMeta.__name__)
print('MyMeta.__bases__: ', MyMeta.__bases__)
print('MyMeta.__bases__: ')
pprint(MyMeta.__dict__)


class MM(MyMeta):
    pass


mm = MM()
print('mm.x = ', mm.x)
print('mm.y = ', mm.y)
print(mm.__class__)
print(mm.__class__.__bases__)


print('=' * 50)

"""
=================================================================
Другая запись (другой способ) создания точно такого же метакласса
"""


class MyMeta2(list, metaclass=type):
    x = 5
    y = 6


print('type(MyMeta):     ', type(MyMeta2))
print('MyMeta.__name__:  ', MyMeta2.__name__)
print('MyMeta.__bases__: ', MyMeta2.__bases__)
print('MyMeta.__bases__: ')
pprint(MyMeta2.__dict__)


