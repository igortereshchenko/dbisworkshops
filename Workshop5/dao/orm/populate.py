from dao.orm.model import *
from dao.db import OracleDb

import random
import hashlib

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)
session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormUserToken).delete()
session.query(ormToken).delete()
session.query(ormUser).delete()

# populate database with new rows
user1 = ormUser( user_name = 'Paul',
                 user_surname = 'Smith',
                 user_email = 'paul_smith1979@mail.com',
                 user_phone = '+04954379201365',
                 user_password = 'password1234',
                 end_date = '20-05-2020')

user2 = ormUser( user_name = 'John',
                 user_surname = 'Pattriks',
                 user_email = 'williWonka2000@aol.com',
                 user_phone = '+08439205728348',
                 user_password='John2001patt'
                 )

user3 = ormUser( user_name = 'Bill',
                 user_surname = 'Fence',
                 user_email = '19microbilltop@gmail.com',
                 user_phone = '+57678987654563',
                 user_password='uncleANNY7'
                 )

user4 = ormUser( user_name = 'Michael',
                 user_surname = 'Waznowski',
                 user_email = 'MichaelWaznowski@protonmail.com',
                 user_phone = '+67493857394857',
                 user_password='thfd23dsDk',
                 )

def hashing(user_id, user_name, user_surname, user_email, user_phone = 0):
    string = str(user_id) + str(user_name) + str(user_surname) + str(user_email) + str(user_phone)
    mix = ''.join(random.sample(string,len(string)))
    result = hashlib.sha256(mix.encode())
    return result.hexdigest()

token1 = ormToken(user_token = hashing(user1.user_id, user1.user_name, user1.user_surname, user1.user_email, user1.user_phone))

token2 = ormToken(user_token = hashing(user2.user_id, user2.user_name, user2.user_surname, user2.user_email, user2.user_phone))

token3 = ormToken(user_token = hashing(user3.user_id, user3.user_name, user3.user_surname, user3.user_email, user3.user_phone))

token4 = ormToken(user_token = hashing(user4.user_id, user4.user_name, user4.user_surname, user4.user_email, user4.user_phone))


# create relations
user1.orm_token.append(token1)
user2.orm_token.append(token2)
user3.orm_token.append(token3)
user4.orm_token.append(token4)

session.add_all([token1, token2, token3, token4, user1, user2, user3, user4])
session.commit()