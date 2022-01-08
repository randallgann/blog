from config import config
from flask import Flask, render_template
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name: str):
    """The application factory"""
    app = Flask(__name__)

    # the config attribute of the Flask object
    # where you can customize configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # mail.init_app(app)
    # moment.init_app(app)
    db.init_app(app)

    # attach routes and custom error pages here

    # blueprint is registered with the application
    # adds a class flask.blueprints.Blueprint at the same level as app
    from .main import main as main_blueprint

    # this adds the main_blueprint class to
    # locals/app/blueprints: dict
    app.register_blueprint(main_blueprint)

    return app


# @app.route("/")
# def index():
#    title = "Homepage Title"
#    paragraph = "Homepage Description"
#    try:
#        return render_template("index.html.jinja", title=title, paragraph=paragraph)
#    except Exception as e:
#        return str(e)


# @app.route("/user")
# def user():
#    try:
#        return render_template("user.html.jinja")
#    except Exception as e:
#        return str(e)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080, passthrough_errors=True)
