import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from apps.config.config import config_by_name

environment = os.getenv("FLASK_ENV") or "development"

db = SQLAlchemy()
migrate = Migrate()


def register_blueprint(app):
    from apps.core.core_blueprint import core_blueprint
    from apps.authentication.authentication_blueprint import authentication_blueprint
    from apps.shortner.shortner_blueprint import shortner_blueprint

    app.register_blueprint(core_blueprint)
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(shortner_blueprint)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[environment])

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)

    register_blueprint(app=app)

    return app


configuration = config_by_name[environment]
