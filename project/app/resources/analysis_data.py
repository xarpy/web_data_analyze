import os

import pandas as pd

from app.models.core import Logs
from app.schemas import DataSetSchema
from app.utils import format_string_for_snake, register_log, send_reponse
from dotenv import find_dotenv, load_dotenv
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename

# Method to get information into .env file!
load_dotenv(find_dotenv())

# Definitions for security
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    """Function to build name of file with location path to folder"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class DataAnalyze(Resource):
    """Resource to receive file .csv"""

    def post(self):
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                path = os.path.join(UPLOAD_FOLDER, filename)

                data = pd.read_csv(path)

                new_col = list()
                for i in data.columns:
                    new_col.append(format_string_for_snake(i))

                data.columns = new_col
                converted = data.to_dict("records")

                # To excluded dataset, because this occuped a lot expansive memory!
                del data

                schema = DataSetSchema(many=True)
                errors = schema.validate(converted)
                register_log(filename, errors)

                return send_reponse({"message": "Dataset analyzed"}, 200)
        except FileNotFoundError:
            return send_reponse({"message": "File not Found"}, 404)
        except Exception as e:
            return send_reponse({"message": f'{e}'}, 500)


class DataLog(Resource):
    """Resource to get all list of errors into db"""

    def get(self):
        return send_reponse(Logs.objects.all(), 200)
