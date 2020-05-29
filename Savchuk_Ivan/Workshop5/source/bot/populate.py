import datetime
import time

from model import *
from OracleDb import OracleDb

db = OracleDb()

session = db.sqlalchemy_session
'''
new_comment = comments.add_member(film="Pulp Fiction",
                                  text="Its great!")

new_snack = snack.add_member(name='popcorn',
                             price=7,
                             orders_num=500,
                             age_limit=0)
a = ['big cola + medium popcorn', 'small beer + chips', 'medium cola + medium popcorn']
b = [500, 340, 1200]
c = [0, 21, 0]
for i in range(len(a)):
    new_snack = snack.add_member(name=a[i],
                                 price=7,
                                 orders_num=b[i],
                                 age_limit=c[i])

new_movie = films.add_member(name='Pulp Fiction',
                             age_limit=18)

new_cinema = cinema.add_member(name='Multiplex',
                               location='Kyiv',
                               orders_num=2000)
new_cinema = cinema.add_member(name='Blockbuster',
                               location='Kyiv',
                               orders_num=3000)
new_cinema = cinema.add_member(name='Florencia',
                               location='Kyiv',
                               orders_num=1000)
new_cinema = cinema.add_member(name='Multiplex',
                               location='Dnipro',
                               orders_num=3000)
new_cinema = cinema.add_member(name='Blockbuster',
                               location='Dnipro',
                               orders_num=6000)
new_cinema = cinema.add_member(name='Florencia',
                               location='Dnipro',
                               orders_num=500)
new_cinema = cinema.add_member(name='Multiplex',
                               location='Odessa',
                               orders_num=1500)
new_cinema = cinema.add_member(name='Blockbuster',
                               location='Odessa',
                               orders_num=4000)
new_cinema = cinema.add_member(name='Florencia',
                               location='Odessa',
                               orders_num=2500)

new_member = app_user.add_member(name='Vanya',
                                 age=20,
                                 phone='+380951601805',
                                 mail='vanya@gmail.com',
                                 bank=1234567890123456,
                                 status='student')

new_order = orders.add_member(film='Pulp Fiction',
                              cinema='Multiplex',
                              phone='+380951601805',
                              seat='4-7',
                              date='26.05.2020',
                              time='10:00',
                              price=12)

new_comment = comments.add_member(film="Reservoir dogs",
                                  text="Great!")
new_comment = comments.add_member(film="Reservoir dogs",
                                  text="Love that!")
new_comment = comments.add_member(film="Reservoir dogs",
                                  text="Tarantino doing best!")

new_comment = comments.add_member(film="Your name",
                                  text="What a story!")
new_comment = comments.add_member(film="Your name",
                                  text="I am crying!")
new_comment = comments.add_member(film="Your name",
                                  text="Tradegy!")

new_movie = films.add_member(name='Reservoir dogs',
                             age_limit=18)
new_movie = films.add_member(name='Your name',
                             age_limit=0)

m = db.execute("SELECT comment_text FROM comments WHERE film = '{}'".format('Reservoir dogs'))
comms = [row[0] for row in m][:3]
new_member = app_user.add_member(name='Vanya',
                                 age=20,
                                 phone='+380951601805',
                                 mail='vanya@gmail.com',
                                 bank=1234567890123456,
                                 status='student')

new_order = orders.add_member(film='Pulp Fiction',
                              cinema='Multiplex',
                              phone='+380951601805',
                              seat='5-8',
                              date='26.05.2020',
                              time='10:00',
                              price=5)
'''
go_data = db.execute(f" SELECT seat FROM orders INNER JOIN app_user ON orders.user_id = app_user.user_id WHERE datte = '{'2020-05-29'}' AND time = '{'16:00'}' AND city ='{'Kyiv'}'")
taken_seats = [row[0] for row in go_data][0]
print(taken_seats)
session.commit()
