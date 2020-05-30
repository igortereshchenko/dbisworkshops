import datetime
import time

from model import *
from OracleDb import OracleDb

db = OracleDb()

session = db.sqlalchemy_session
'''
new_comment = comments.add_member("Pulp Fiction", "Its great!")
new_dish = dish.add_member('Florencia', '......', 4.5, 100)
new_user = app_user.add_member(name='Scarab', age=18,
                               phone='+38095323232',
                               age='18',
                               mail='scarab@bdis.com',
                               bank='12234445543333',
                               orders_num=1)
new_order = orders.add_member(dish_name='AAAAAA',
                              phone='+38095323232',
                              
'''
session.commit()
