from baymax_backend import app
from baymax_backend.database import db_session
from baymax_backend.models import User
from flask_restful import Resource, Api, abort
from flask import request
import pickle
import pandas as pd
from baymax_backend.schemas import UserSchema
from os import path
import sys

api = Api(app)


class CardiacAPI(Resource):
    # shows the list of all users
    def post(self):
        req_data = request.get_json()
        req_data = {k: [int(v)] for k, v in req_data.items()}
        basepath = path.dirname(__file__)
        model_path = basepath + '/heart_failure_model.sav'
        loaded_model = pickle.load(open(model_path, 'rb'))
        df2 = pd.DataFrame.from_dict(data=req_data)
        result = float("{:.2f}".format(float(loaded_model.predict_proba(df2)[0][1]))) * 100
        return result


class KidneyAPI(Resource):
    # shows the list of all users
    def post(self):
        req_data = request.get_json()
        req_data = {k: [int(v)] for k, v in req_data.items()}
        basepath = path.dirname(__file__)
        model_path = basepath + '/chronic_kidney_model.sav'
        loaded_model = pickle.load(open(model_path, 'rb'))
        df2 = pd.DataFrame.from_dict(data=req_data)
        result = float("{:.2f}".format(float(loaded_model.predict_proba(df2)[0][1])))*100
        return result


# Setup the Api resource routing here
api.add_resource(CardiacAPI, '/cardiac')
api.add_resource(KidneyAPI, '/kidney')

# curl http://localhost:5000/user
# curl -H "Content-Type: application/json" -X POST -d '{"first_name": "girish","last_name": "shan","email": "girish@gmail.com","phone": "9566646916" }'  http://localhost:5000/user
# curl http://localhost:5000/user/1 -X DELETE
# curl -H "Content-Type: application/json" -X PUT -d '{"first_name": "girish" }'  http://localhost:5000/user/2