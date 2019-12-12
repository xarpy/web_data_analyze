# -*- coding: utf-8 -*-
import logging
import os
from datetime import timedelta

from dotenv import find_dotenv, load_dotenv

# Method to get information into .env file!
load_dotenv(find_dotenv())


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    MONGODB_DB = os.getenv('DB_NAME')
    MONGODB_HOST = os.getenv('DB_HOST')
    MONGODB_PORT = os.getenv('DB_PORT')
    MONGODB_USERNAME = os.getenv('DB_USERNAME')
    MONGODB_PASSWORD = os.getenv('DB_PASSWORD')
    MONGODB_CONNECT = False
    LOGGING_LOCATION = os.getenv('LOG')
    LOGGING_LEVEL = logging.DEBUG
    PROPAGATE_EXCEPTIONS = True


class Development(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class Testing(Config):
    FLASK_ENV = 'testing'
    TESTING = True
    DEBUG = True


class Production(Config):
    FLASK_ENV = 'production'
    TESTING = False
    DEBUG = False


config = {
    'development': Development,
    'testing': Testing,
    'default': Production
}


def configure(app):
    config_name = os.getenv("FLASK_ENV") or "default"
    app.config.from_object(config[config_name])
    # Configuring logging
    # Gunicorn
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    # Flask
    handler = logging.FileHandler(app.config["LOGGING_LOCATION"])
    handler.setLevel(app.config["LOGGING_LEVEL"])
    formatter = logging.Formatter(app.config["LOGGING_FORMAT"])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
