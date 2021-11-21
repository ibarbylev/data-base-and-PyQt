from sqlalchemy import __version__, create_engine, Table, Column, \
    Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

from exp_6 import User, METADATA, ENGINE, SESS_OBJ

# ******************* C R U D ******************
# ******************* Create *******************
# ******************* Retrieve *****************
# ******************* Update *******************
# ******************* Delete *******************

# create
user_2 = User('Иван', 'Иванов', 'asdf')
SESS_OBJ.add(user_2)
SESS_OBJ.commit()

# # retrieve
result = SESS_OBJ.query(User).filter_by(name='Иван')
print('total rows: ', result.count())
print(result.all())
#
# # update 1 row
# result.first().password += '1'
# SESS_OBJ.commit()
#
#
# # update multiple lines simultaneously var #1
# for row in result.all():
#     row.password += "1"
# SESS_OBJ.commit()
#
# # update multiple lines simultaneously variant #2
# result.update({User.password: 555})
# SESS_OBJ.commit()
#
# # delete
# result.delete()
# SESS_OBJ.commit()


