# -*- coding: utf-8 -*-

from config import configure as config_project
from flask import Flask
from flask_cors import CORS

from .api import configure as config_api
from .models.core import configure as config_db


def create_app(config_name):

    app = Flask(__name__)

    '''Added Configurations'''
    config_project(app)
    config_api(app)
    config_db(app)

    '''Added Thirds'''
    CORS(app)

    return app
