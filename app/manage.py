from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db

manager = Manager(app)
