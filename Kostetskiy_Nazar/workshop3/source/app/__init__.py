import logging
from flask import Flask
from flask_login import LoginManager

from app.db_models.base import AppBase, engine
from app.db_models import User
from config import DB_URL_PATH, DEBUG, SECRET_KEY
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_socketio import SocketIO

logger = logging.getLogger(__name__)

app = Flask(__name__)
socketio = SocketIO(app, logger=logger, async_mode="gevent")

app.debug = DEBUG
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

AppBase.metadata.create_all(engine)
migrate = Migrate(app, AppBase)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(app)

from app import views
