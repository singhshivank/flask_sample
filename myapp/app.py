from flask import Flask, request
from flask_restplus import Api, Resource
import constants as Constants
import requests,os,sys
from protobuf_integration import ProtobufService


app = Flask(__name__)
api = Api(app, version='1.0', title='Proto API', description='Protobuf service API',)
# api = Api(app=app)
ns_conf = api.namespace('activate-account', description='Service API operations')

parser = api.parser()
parser.add_argument('data', type=str, required=True, help='Protobuff encrypted payload', location='json')

@ns_conf.route("/")
class ConferenceList(Resource):

    @api.doc(parser=parser)
    def post(self):
        """
        Request protobuf data to JAVA api
        """
        proto_payload = request.json['data']

        # token = request.headers['authorization']
        # headers={'Authorization': token}
        # response = requests.get(url = Constants.ACTIVE_ACCOUNT, data=jsonObj, headers = headers)

        return proto_payload


# @ns_conf.route("/<int:id>")
# @api.doc(params={'id': 'An ID'})
# class Conference(Resource):
#     def get(self, id):
#         """
#         Displays a conference's details
#         """
#     def post(self, id):
#         """
#         Create a new user
#         """

if __name__ == "__main__":
    app.run()
