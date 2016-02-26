import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print BASE_DIR
SQLALCHEMY_ECHO = False
dbpath = os.path.join(BASE_DIR, 'app.db')
print dbpath
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + dbpath
SQLALCHEMY_TRACK_MODIFICATIONS = False
PORT = 8080
HOST = '0.0.0.0'
DEBUG = True
SECRET_KEY = 'secret'
CSRF_ENABLED = True
