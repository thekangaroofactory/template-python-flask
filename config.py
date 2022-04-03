"""Flask configuration."""
from os import path

basedir = path.abspath(path.dirname(__file__))

# Test & Debug
TESTING = True
DEBUG = True
KANGAROO_ID = 'KANGAROO_ID'


# Flask
# FLASK_APP = 'wsgi.py'
FLASK_ENV = 'development'
#SECRET_KEY = 'xxx'

# Database


# Application
#UPLOAD_FOLDER = '/xxx'
