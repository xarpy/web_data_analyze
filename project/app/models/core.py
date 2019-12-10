# -*- coding: utf-8 -*-

'''[Models: Core]
Neste arquivo, temos a estrutura principal do APP.
'''
from datetime import datetime

from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form

db = MongoEngine()


def configure(app):
    db.init_app(app)
    app.db = db

# TODO: Falta criar a base do mongo!!


class Logs(db.Document):
    pass
