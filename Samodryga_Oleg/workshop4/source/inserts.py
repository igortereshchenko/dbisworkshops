from classes import *

db = OracleDb()

session = db.sqlalchemy_session

new_user = Users()
new_country = Country.add_country('USA')
new_user.add_user('Name', '11111', 'USA')
new_numbers_aid = NumbersAid.add_aidNumber('+38975452', 'USA')
new_hospital = Hospital.add_hospital('NameHospital','Some adress', 'USA')
new_symptom = Symptom.add_symptom('SyptomName', 'Desc')
new_note = Note.add_note('NoteName', 'Desc', new_user.id)

session.commit()