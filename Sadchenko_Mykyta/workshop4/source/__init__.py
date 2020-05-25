from flask import Flask
from Sadchenko_Mykyta.workshop4.source.dao.config import Config
from Sadchenko_Mykyta.workshop4.source.OracleDb import OracleDb

app = Flask(__name__)
app.config.from_object(Config)
db = OracleDb()

from Sadchenko_Mykyta.workshop4.source import routes

