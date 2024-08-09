import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

from app import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    app = Flask(__name__)
    config_name = config_name or os.getenv('FLASK_ENV', 'default')
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    # Set up logging based on the configuration
    logging.basicConfig(level=app.config['LOG_LEVEL'],
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        handlers=[logging.StreamHandler()])

    with app.app_context():
        from app import routes, models
        routes.register_routes(app)
        db.create_all()

    return app