"""А теперь посмотрим как создать метакласс для своих пользовательских классов"""

"""
Представьте, что мы устали от задания атрибутов в конструкторе 
__init__(self, *args, **kwargs). 
Как бы сделать так, чтобы мы смогли задавать атибуты непосредственно 
при создании экземпляра класса
"""

# Обычный класс такое не позволит


class MyClass:
    pass


#MC = MyClass(param_1=100, param_2=200)


"""
Вспомним, что объект создается через вызов класса с помощью оператора "()"
Создадим метакласс наследованием от type
Метакласс будет переопределять данный оператор "()"
"""


class AttrOptim(type):
    def __call__(self, *args, **kwargs):
        """ Вызов класса создает новый объект. """
        # Перво-наперво создадим сам объект...
        obj = type.__call__(self, *args)
        # ...и добавим ему переданные в вызове аргументы в качестве атрибутов.
        for name in kwargs:
            setattr(obj, name, kwargs[name])
            # вернем готовый объект
        return obj


# Теперь создадим класс, использующий новый метакласс
class MyClass(metaclass=AttrOptim):
    pass


# Ура!!!
MC = MyClass(param_1=100, param_2=200)
print(MC.__dict__)
print(MC.param_1)
print(MC.param_1)


### Внимание ###
"""
Всё что угодно является объектом в Питоне: 
экземпляром класса или экземпляром метакласса.

Кроме type!!!!!

type является собственным метаклассом. 
Это нельзя воспроизвести на чистом Питоне и делается небольшим читерством на уровне реализации.

Во-вторых, метаклассы сложны. Вам не нужно использовать 
их для простого изменения классов. Это можно делать двумя разными способами:
-руками
-декораторы классов

В 99% случаев, когда вам нужно изменить класс, лучше использовать эти два.
"""