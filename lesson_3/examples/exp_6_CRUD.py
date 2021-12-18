"""
Для того, чтобы свободно чувствовать себя с любой БД
необходимо овладеть операциями CRUD:

C - Create
R - Retrieve
U - Update
D - Delete

"""

from exp_6 import User, sess


# create
user_2 = User('Пётр', 'Петров', 'pass_Petrov')
sess.add(user_2)
sess.commit()

# # Retrieve
result = sess.query(User).filter_by(name='Пётр')
print('total rows: ', result.count())
print(result.all())
#
# # Update 1 row
# result.first().password += '1'
# sess.commit()
#
#
# # Update multiple lines simultaneously var #1
# for row in result.all():
#     row.password += "1"
# sess.commit()
#
# # Update multiple lines simultaneously variant #2
# result.update({User.password: 555})
# sess.commit()
#
# # Delete
# result.delete()
# sess.commit()

"""
**************************** ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ *************************************
Более подробно о всех командах и методах можно прочитать в русскоязычном описании SQAlchemy
https://lectureswww.readthedocs.io/6.www.sync/2.codding/9.databases/2.sqlalchemy/
********************************************************************************************
"""
