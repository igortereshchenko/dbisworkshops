import datetime
from Sadchenko_Mykyta.workshop4.source.models import (
		User, Note, UserNoteParams, PrivateAccess
	)
from Sadchenko_Mykyta.workshop4.source.OracleDb import OracleDb

db = OracleDb()

session = db.sqlalchemy_session
'''
new_user = User(username='Bob',
				password='ex@gmail.com',
				email=form.email.data)
new_note = Note(url_id='123abc789',
				title='ABCADsdmkf;daf',
				text='Lorem impsum...')
new_params = UserNoteParams(change_possibility='T',
						private_access='F',
						encryption='T',
						note_id=1,
						user_id=1)
new_access = PrivateAccess(note_id=1,
						user_id=1)
'''
session.commit()
