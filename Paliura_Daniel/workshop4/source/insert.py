from classes import *

db = OracleDb()

session = db.sqlalchemy_session

User.add_user("Daniel", "ru", "disgusting", "password1", "Paliura")
User.add_user("Alexandr", "cs", "seshue", "password2", "Podolskiy")
session.commit()

Dialog.add_dialog(1,2)
session.commit()

Message.add_message(1, 1, 2, "ru", "cs", "Привет!", "Nazdar!")
session.commit()