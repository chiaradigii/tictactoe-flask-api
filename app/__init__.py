import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

from app import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    from flask import Flask
    import os
    from . import config, db, migrate  # Ensure these are correctly imported
    import logging

    app = Flask(__name__)
    config_name = config_name or os.getenv('FLASK_ENV', 'default')
    
    # Use getattr to safely get the configuration object
    app_config = getattr(config, config_name, None)
    if app_config is None:
        raise ValueError(f"Invalid configuration name: {config_name}")
    app.config.from_object(app_config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Set up logging based on the configuration
    logging.basicConfig(level=app.config['LOG_LEVEL'],
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        handlers=[logging.StreamHandler()])

    with app.app_context():
        from . import routes, models  # Adjusted import to be relative
        routes.register_routes(app)
        db.create_all()

    return app