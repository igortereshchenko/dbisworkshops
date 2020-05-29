import datetime
import time

from model import *
from OracleDb import OracleDb

db = OracleDb()

session = db.sqlalchemy_session

#       Creating data for tables

'''
                Movies
'''

new_comment = comments.add_member(film="Pulp Fiction",
                                  text="Its great!")
new_movie = films.add_member(name='Reservoir dogs',
                             age_limit=18)
new_movie = films.add_member(name='Your name',
                             age_limit=0)
new_movie = films.add_member(name='Rock star',
                             age_limit=0)

'''
                Snacks
'''

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

'''
                Cinema
'''

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

'''
                Comments
'''

new_comment = comments.add_member(film="Reservoir dogs",
                                  text="Great!")
new_comment = comments.add_member(film="Reservoir dogs",
                                  text="Love that!")
new_comment = comments.add_member(film="Reservoir dogs",
                                  text="Tarantino doing best!")

new_comment = comments.add_member(film="Pulp Fiction",
                                  text="So much blood...")
new_comment = comments.add_member(film="Pulp Fiction",
                                  text="Big guns!")
new_comment = comments.add_member(film="Pulp Fiction",
                                  text="Great!")

new_comment = comments.add_member(film="Your name",
                                  text="What a story!")
new_comment = comments.add_member(film="Your name",
                                  text="I am crying!")
new_comment = comments.add_member(film="Your name",
                                  text="Tradegy!")

new_comment = comments.add_member(film='Rock star',
                                  text="Woah!")
new_comment = comments.add_member(film='Rock star',
                                  text="Like such style!")
new_comment = comments.add_member(film='Rock star',
                                  text="Great stuff!")

session.commit()
