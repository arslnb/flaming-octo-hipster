from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import nit, db

nit.config.from_pyfile('configure.py')
migrate = Migrate(nit, db)
manager = Manager(nit)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()




