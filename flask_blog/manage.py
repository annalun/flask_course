# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server #changed
from flask_migrate import MigrateCommand #changed
from flask_blog import app

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = 'localhost', #changed
    port = 5000) #changed
)

if __name__ == "__main__":
    manager.run()
