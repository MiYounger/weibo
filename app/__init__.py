from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
#from config import Config, basedir
import config
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
db.create_all()
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models