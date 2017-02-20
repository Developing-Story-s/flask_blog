import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask_blog import app

manager = Manager(app)

manager.add_command("runserver", Server(
            use_debugger = True,
            use_reloader = True,
            host = os.getenv('IP', '127.0.0.1'),
            port = int(os.getenv('PORT', 5000))
        ))

from flask_blog import db

if __name__ == "__main__":
    # db.session.commit()
    db.create_all()
    db.session.flush()
    manager.run()
    db.create_all()
    db.session.flush()
    manager.run()
