from root.source.ORM_relations import *
from datetime import datetime

user = orm_users.add('admin','admin',1)
orm_config.add(user.id, 5, 5, 10, 20, 5, 5)
orm_items.add(user.id, 'M4S1', 10.23, 'Sold')
orm_actions.add(user.id, 'withdraw', datetime.now())