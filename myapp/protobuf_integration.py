import requests,os,sys
import base64, json
from utility import switchtech_payloads_pb2 as ProtoDefination
from google.protobuf.json_format import MessageToJson
from utility import response_converter_pb2 as ResponseConverter
from google.protobuf.json_format import Parse

class ProtobufService:

    def proto_to_json(self):
        my_list = ProtoDefination.ActivateAccount()
        my_list.ParseFromString(base64.b64decode(payload_data))
        jsonObj = MessageToJson(my_list)
        return jsonObj

    def json_to_proto(self):
        message = Parse(json.dumps(response.json()), ResponseConverter.data())
        response_data = base64.b64encode(message.SerializeToString()).decode()
        return response_data
