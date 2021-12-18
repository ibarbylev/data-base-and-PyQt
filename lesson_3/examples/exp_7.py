"""
ORM с помощью SQLAalchemy.
ВАРИАНТ 2: ДЕКЛАРАТАВНЫЙ СТИЛЬ"
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///declarative_style_base.db3', echo=True)

# Функция declarative_base(), что определяет новый класс Base,
# от которого будут унаследованы все наши ORM-классы.
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return f'<User({self.name}, {self.fullname}, {self.password})>'


user = User("Иван", "Иванов", "pass_Ivan")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sess = Session()

sess.add(user)
sess.commit()
print(user.id)  # -> 2
