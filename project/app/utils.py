# -*- coding: utf-8 -*-

'''
Neste arquivo, temos as funções recorrentes para todos os clientes.
'''
import re
from os.path import dirname, join

from app.models.core import Logs
from flask import Response, json


def format_string_for_snake(string):
    """Format any string, excluded special character and convert to patterns snake case"""
    regex = re.compile('[@!#$%^&*()<>?\|}{~:]')
    if(regex.search(string) == None):
        s = string.replace(" ", "_")
        return s.replace("/", "_")

    else:
        result = regex.sub("", string).casefold().replace(" ", "_")
        return result.replace("/", "_")

# TODO: Retirar contexto
# def pagination(data, url, start, limit):
#     count = len(data)
#     if (count < start):
#         abort(404)
#     return dict(
#         start=start,
#         limit=limit,
#         count=count,
#         message=data[(start - 1):(start - 1 + limit)],
#     )


def register_log(filename, list_errors):
    log = LogApi(name_file=filename, errors=list_errors)


def send_reponse(msg, code, headers=None):
    send = Response(
        response=json.dumps(msg),
        status=code,
        mimetype='application/json'
    )
    if headers is not None:
        send.headers.add(headers[0], headers[1])
    return send

# TODO: Analisar uso e contexto
# def get_local_env():
#     path = join(dirname(__file__), '.env')
#     return path
