from config import config
from flask import Flask, render_template
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# mail = Mail()
# moment = Moment()
# db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # mail.init_app(app)
    # moment.init_app(app)
    # db.init_app(app)

    # attach routes and custom error pages here

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    # Import Dash application
    from .plotlydash.dashboard import init_dashboard

    app = init_dashboard(app)

    return app
