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

# =================================================
# ПЕРЕНЕСТИ В ДРУГОЙ !!!!!!!!!!!!!!!!11

print('=' * 50)

"""
Итак, метакласс создан. Теперь, чтобы получить экземпляр этого класса,
мы используем скобки, то есть по сути вызываем метод __call__:
"""

NewClass = MyMeta()

"""
Метод __call__ автоматически вызывает ещё два метода: 
__new__  - используется, когда надо проконтролировать создание нового экземпляра класса
           Это - первый шаг в создании нового экземпляра класса, который и
           возвращает этот экземпляр. 
__init__ - в отличии от __new__ ничего не возвращает, а только инициализирует
           уже созданный экземпляр класса
"""


class MyMeta_2(type):
    def __new__(cls, name, bases, dct):
        ex = super().__new__(cls, name, bases, dct)
        ex.x = 5
        ex.y = 6
        return ex

# ex = MyMeta_2('ex', (list, ), dict(x=5, y=6))
#
# print('type(MyMeta):     ', type(ex))
# print('MyMeta.__name__:  ', ex.__name__)
# print('MyMeta.__bases__: ', ex.__bases__)
# print('MyMeta.__bases__: ')
# pprint(ex.__dict__)
