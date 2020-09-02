from flask import Flask, request
from flask_restplus import Api, Resource
import constants as Constants
import requests,os,sys


app = Flask(__name__)
api = Api(app=app)
ns_conf = api.namespace('activate-account', description='Service API operations')

@ns_conf.route("/")
class ConferenceList(Resource):

    def post(self):
        """
        Request protobuf data to JAVA api
        """
        proto_payload = request.json['data']

        token = request.headers['authorization']
        headers={'Authorization': token}
        response = requests.get(url = Constants.ACTIVE_ACCOUNT, data=jsonObj, headers = headers)

        return response


# @ns_conf.route("/<int:id>")
# class Conference(Resource):
#     def get(self, id):
#         """
#         Displays a conference's details
#         """
#     def put(self, id):
#         """
#         Edits a selected conference
#         """

if __name__ == "__main__":
    app.run()
