# -*- coding: utf-8 -*-

from os import getenv

from app import create_app
from app.models.core import db
# from app.utils import get_local_env
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = create_app(getenv('FLASK_ENV') or 'default')


@app.shell_context_processor
def shell_context():
    return dict(
        app=app,
        db=db,
    )
