# this is the main script
# where the application instance is defined
# in the top level directory

import os

from flask_migrate import Migrate

# create_app function
# db class
from app import create_app  # , db

##### TO DO #######
# implement User, Role
# from app.models import User, Role


# app is class 'flask.app.Flask'
app = create_app(os.getenv("FLASK_CONFIG") or "default")
# app = create_app("development")

# migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)  # TO DO ### implement (db=db, User=User, Role=Role)
