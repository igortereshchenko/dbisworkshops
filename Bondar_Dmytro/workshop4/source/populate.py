from classes import *

db = OracleDb()

session = db.sqlalchemy_session

new_user = User()
new_user.add_user('111111', 'bo1111bov', 'bo11bovich')
new_event = Event.add_event(new_user.id, 'Para', '22/05/2020', '14:00', '15:00', tue='1')
new_group = Group.add_group(new_user.id, 'KM-73')

session.commit()