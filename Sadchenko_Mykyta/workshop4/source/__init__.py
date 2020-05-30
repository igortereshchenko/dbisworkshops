from flask import Flask
from Sadchenko_Mykyta.workshop4.source.dao.config import Config
from Sadchenko_Mykyta.workshop4.source.dao.OracleDb import OracleDb

app = Flask(__name__)
app.config.from_object(Config)
db = OracleDb()

from Sadchenko_Mykyta.workshop4.source import routes

from notes import db
from notes.models import User, Note
nu = User('123','12@dsa.sd','123')
db.session.add(nu)
db.session.commit()
