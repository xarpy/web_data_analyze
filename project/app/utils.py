# -*- coding: utf-8 -*-

import re
from os.path import dirname, join

from app.models.core import Logs
from flask import Response, json


def format_string_for_snake(string):
    """Format any string, excluded special character and convert to patterns snake case"""
    regex = re.compile('[@!#$%^&*()<>?\|}{~:]')
    if(regex.search(string) == None):
        s = string.replace(" ", "_")
        return s.replace("/", "_").casefold()

    else:
        result = regex.sub("", string).casefold().replace(" ", "_")
        return result.replace("/", "_")


def register_log(filename, list_errors):
    """Register object log into collection Logs"""
    log = Logs(name_file=filename, errors=json.dumps(list_errors)).save()


def send_reponse(msg, code, headers=None):
    """function to send response with all customization"""
    send = Response(
        response=json.dumps(msg),
        status=code,
        mimetype='application/json'
    )
    if headers is not None:
        send.headers.add(headers[0], headers[1])
    return send
