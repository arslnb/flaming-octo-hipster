from flask import Flask
from flask.exit.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

nit = Flask(__name__instance_relative_config=True)
nit.config.from_pyfile('config.py')

db = SQLAlchemy(nit)

migrate = Migrate(nit, db)
manager = Manager(nit)
manager.add_command('db', MigrateCommand)

import routes