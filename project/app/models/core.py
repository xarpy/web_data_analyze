# -*- coding: utf-8 -*-

from datetime import datetime

from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from mongoengine import DateTimeField, ListField, StringField

db = MongoEngine()


def configure(app):
    db.init_app(app)
    app.db = db


class Logs(db.Document):
    """Model for Logs"""
    name_file = StringField(required=True)
    errors = ListField(required=True)
    created = DateTimeField(default=datetime.now)
