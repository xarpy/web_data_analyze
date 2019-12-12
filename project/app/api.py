from app.resources.analysis_data import DataAnalyze, DataLog
from flask_restful import Api

api = Api()


def configure(app):
    """[sumary]
    This functions is initially all resources created for arquitecture Restful
    """
    api.add_resource(DataAnalyze, '/data/insert')
    api.add_resource(DataLog, '/data/logs')
    api.init_app(app)
