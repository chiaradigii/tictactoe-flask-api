import os
import logging

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///tic_tac_toe.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
    LOG_LEVEL = logging.DEBUG  

class ProductionConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/your_database'
    LOG_LEVEL = logging.INFO  

development = DevelopmentConfig
production = ProductionConfig

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
