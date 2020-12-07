import os
from app import create_app, db
import logging.config, yaml
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
import logging, logging.config

__author__ = 'tomas'

app = create_app(os.getenv('FLASK_ENV') or 'default')
manager = Manager(app)
migrate = Migrate(app, db, directory='db/migrations')


# python weather_manager.py deploy
@manager.command
def deploy():
    print("Run deployment tasks")

def make_shell_context():
    return dict(app=app, db=db)  # these objects can be used in shell


manager.add_command("shell", Shell(make_context=make_shell_context))  # python3 weather_manager.py shell

# first time run
# python weather_manager.py db init
# python weather_manager.py db migrate
# python weather_manager.py db upgrade
# python weather_manager.py db (init / upgrade / migrate -m "initial migration")
manager.add_command('db', MigrateCommand)


# python weather_manager.py runserver
if __name__ == '__main__':
    # logging.basicConfig(filename='./log/error.log',level=logging.DEBUG)
    logging.config.dictConfig(yaml.load(open('./log/logging.conf')))

    # output log to file
    error_log_file = logging.getLogger('error_file')
    # error_log_file.error("Error FILE")

    info_log_file = logging.getLogger('info_file')
    # info_log_file.info("Info FILE")

    # logconsole = logging.getLogger('console')
    # logconsole.debug("Debug CONSOLE")
    manager.add_command('runserver', Server(host='192.168.1.9', port=5010))
    manager.run()