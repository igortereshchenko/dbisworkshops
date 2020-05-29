import datetime
import time

from model import *
from OracleDb import OracleDb

db = OracleDb()

session = db.sqlalchemy_session
'''
new_comment = comments.add_member("Pulp Fiction", "Its great!")
new_cinema = cinema.add_member('Florencia', 'Bulvar Perova', 100)
new_film = films.add_member('Pulp Fiction', datetime.date(1994, 5, 21), 18, 100500)
new_ticket = ticket.add_member('Pulp Fiction', 'Florencia', '6-12', datetime.datetime(1994, 5, 21, hour=12, minute=0), 40)
new_user = app_user.add_member(name='Scarab', age=18,
                               phone='+38095323232',
                               mail='scarab@bdis.com',
                               bank='12234445543333',
                               orders_num=1)

new_order = orders.add_member(film_name='Pulp Fiction',
                              cinema_name='Florencia',
                              phone='+38095323232',
                              seat='6-12',
                              time=datetime.datetime(1994, 5, 21, hour=12, minute=0))
'''
session.commit()
