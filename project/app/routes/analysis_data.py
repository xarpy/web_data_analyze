import pandas as pd

from app.utils import format_string_for_snake, send_reponse
from flask import request
from flask_restful import Resource


class DataAnalyze(Resource):
    def post(self):
        try:
            data = pd.read_csv(path)
            old_col = list(data.columns)
            new_col = list()
            for i in old_col:
                new_col.append(format_string_for_snake(i))
            data.columns = new_col
            converted = data.to_dict("records")
            # --------Falta Completar ---------
        except FileNotFoundError:
            return send_reponse({"message": "File not Found"}, 404)
        except Exception as e:
            return send_reponse({"message": e}, 500)
        finally:
            del data


class DataLog(Resource):
    def get(self):
        # ---------- Falta completar o Get na base de logs-----------------
        pass
