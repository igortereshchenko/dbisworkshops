from classes import *

db = OracleDb()

session = db.sqlalchemy_session

new_vendor = Vendors.add_vendor('NameCoshey Local DIY', '11111@i.com', '125')
new_ivent = Ivents.add_ivent('Shoegaze Night', 'Shoegaze', '2020/06/01', '1', '125')

session.commit()