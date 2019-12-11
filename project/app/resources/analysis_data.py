import os

import pandas as pd
from app.models.core import Logs
from app.schemas import DataSetSchema
from app.utils import format_string_for_snake, send_reponse, register_log
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

from dotenv import find_dotenv, load_dotenv

# A partir do arquivo atual adiciona o path do arquivo .env
load_dotenv(find_dotenv())

# Definitions for security
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class DataAnalyze(Resource):
    def post(self, fname):
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = file.save(os.path.join(UPLOAD_FOLDER, filename)

                data=pd.read_csv(path)

                old_col=list(data.columns)
                new_col=list()

                for i in old_col:
                    new_col.append(format_string_for_snake(i))
                data.columns=new_col
                converted=data.to_dict("records")

                schema=DataSetSchema(many=True)
                errors=schema.validate(converted)
                register_log(filename, errors)

                return send_reponse({"message": "Dataset analyzed"}, 200)
        except FileNotFoundError:
            return send_reponse({"message": "File not Found"}, 404)
        except Exception as e:
            return send_reponse({"message": e}, 500)
        finally:
            del data


class DataLog(Resource):
    def get(self):
        return Logs.objects.all()
