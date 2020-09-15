from flask import Flask, request
from flask_restplus import Api, Resource
import constants as Constants
import requests,os,sys
from protobuf_integration import ProtobufService


app = Flask(__name__)
api = Api(app, version='1.0', title='Proto API', description='Protobuf service API',)
# api = Api(app=app)
ns_conf = api.namespace('app', description='Service API operations')

parser = api.parser()
parser.add_argument('data', type=str, required=True, help='Protobuff encrypted payload', location='json')
parser.add_argument('authorization',type=str,required=True, help='token', location='headers')

@ns_conf.route("/v1/activate-account")
class ConferenceListV1(Resource):

    @api.doc(parser=parser)
    def post(self):
        """
        Request protobuf data to JAVA api
        """
        proto_payload = request.json['data']
        proto_obj = ProtobufService()

        data = proto_obj.proto_to_json(proto_payload)
        print("---------->",data,"/n----------------->")

        token = request.headers['authorization']
        # headers={'Authorization': token}
        # response = requests.get(url = Constants.ACTIVE_ACCOUNT, data=proto_obj.proto_to_json(proto_payload), headers = headers)
        # if response['messege'] == "sdohuou":
        #     abort(401, Constants.JAVA_ERROR_RESPONSE)
        # return {"data":json.dumps(response.json())}
        return {"data":"sucess"}

@ns_conf.route("/v2/activate-account")
class ConferenceListV2(Resource):

    @api.doc(parser=parser)
    def post(self):
        """
        Request protobuf data to JAVA api
        """
        return "In version 2"        

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
