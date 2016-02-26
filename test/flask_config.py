import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print 'BASE_DIR: ', BASE_DIR
SQLALCHEMY_ECHO = True
dbpath = os.path.join(BASE_DIR, 'test.db')
print 'dbpath: ', dbpath
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + dbpath
SQLALCHEMY_TRACK_MODIFICATIONS = False
HOST = 'localhost'
PORT = 8080
