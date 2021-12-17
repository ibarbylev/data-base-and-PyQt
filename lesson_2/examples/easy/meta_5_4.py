"""
Следующий пример: контроль имён атрибутов вновь созданного класса Foo
с помощью метакласса ControlAttrName
"""
from pprint import pprint


class ControlAttrName(type):
    # Вызывается для создания экземпляра класса, перед вызовом __init__
    def __init__(cls, future_class_name, future_class_parents, future_class_attrs):
        """
          Return a class object, with the list of its attribute turned
          into uppercase.
        """
        # pick up any attribute that doesn't start with '__' and uppercase it
        required_attributes = ['x', 'y']
        not_found_attributes = required_attributes
        for attr, v in future_class_attrs.items():
            if attr in required_attributes:
                not_found_attributes.remove(attr)

        if not_found_attributes:
            raise AttributeError(f"Not found attributes: {', '.join(not_found_attributes)}")

        super(ControlAttrName, cls).__init__(future_class_name, future_class_parents, future_class_attrs)


class Foo(metaclass=ControlAttrName):  # global __metaclass__ won't work with "object" though
    x = 5


foo = Foo()

# print("hasattr(Foo, 'bar'): ", hasattr(Foo, 'bar'))
# print("hasattr(Foo, 'BAR'): ", hasattr(Foo, 'BAR'))
#
# try:
#     print(Foo.bar)
# except Exception as e:
#     print(f'Exception: {e}')
#
# print('Foo.BAR =', Foo.BAR)
# pprint(Foo.__dict__)
