import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tic_tac_toe.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
