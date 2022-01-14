# application configuration

# import necessary modules
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # setting configuration variables
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    # MAIL_PORT =
    # MAIL_USE_TLS
    # MAIL_USERNAME
    # MAIL_PASSWORD
    # FLASKY_MAIL_SUBJECT_PREFIX
    # FLASK_MAIL_SENDER
    # FLASKY_ADMIN
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # HOST = "0.0.0.0"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASEURL")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)
        # log to stderr - Docker auto captures stderr and exposes through docker logs command
        import logging
        from logging import StreamHandler

        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
    "docker": DockerConfig,
}

# this needs to be tested
