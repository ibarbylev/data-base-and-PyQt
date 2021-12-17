"""
Дескриптор - это объект, определяющий и контролирующий
значение (свойства, поведение) атрибутов экземпляра класса.
Дескриптор определяет методы, которые вызываются в момент доступа к атрибуту
класса. Эти методы могут быть вызваны:
 - при попытке узнать значение атрибута (метод __get__);
 - при попытке присвоить атрибуту новое значение (метод __set__);
 - или при попытке удаления атрибута (метод __delete__).

Иными словами, дескрипторы - это любые объекты, определяющие поведение
атрибутов класса при вызове методов __get__, __set__ или __delete__.

Дескриптор, где используются ТОЛЬКО методы __get__, назывыается "non-data descriptor".
А тот, где наоборот, используются только методы __set__ и/или __delete__,
называется "data descriptor".
"""


class NonNegative:
    """ Этот класс описывает поведение дескрипторов """

    def __init__(self, my_attr):
        # вместо my_attr на самом деле будет hours или rate
        # например, hours и rate
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        # instance - экземпляр класса Worker - <__main__.Worker object at 0x0000008D1B728860>
        # owner - класс Worker - <class '__main__.Worker'>
        # instance.__dict__ - {'name': 'Иван', 'surname': 'Иванов', 'hours': 10, 'rate': 100}

        # получаем значение из словаря атрибутов экземпляра класса
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        # instance - экземпляр класса Worker - <__main__.Worker object at 0x000000E7FFEB8898>
        # value - присваиваемое значение, например 10 или 100 в нашем случае
        if value < 0:
            raise ValueError("Не может быть отрицательным")

        # присваиваем значение атрибуту, если оно прошло валидацию
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        # перехватываем удаление атрибута
        del instance.__dict__[self.my_attr]


class Worker:
    """ Делаем атрибуты дескрипторами """
    # сразу виден недостаток
    # приходится передавать конструктору класса имя атрибута
    hours = NonNegative('hours')
    rate = NonNegative('rate')

    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate

    def total_profit(self):
        return self.hours * self.rate


OBJ = Worker('Иван', 'Иванов', 10, 100)
print(OBJ.total_profit())

OBJ.hours = 10
OBJ.rate = 100
print(OBJ.__dict__)
print(OBJ.total_profit())
del OBJ.rate
print(OBJ.__dict__)

# OBJ = Worker('Иван', 'Иванов', -10, 100)
# print(OBJ.total_profit())

# OBJ.hours = 10
# OBJ.rate = -100
# print(OBJ.total_profit())

# теперь проблема решена
# один класс NonNegative делает нужный атрибут дескриптором
# но эта версия протокола дескриптора - устаревшая
# с версии Python 3.6 появилась новая
