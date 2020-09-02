import switchtech_payloads_pb2 as ProtoDefination
import sys, json, base64
from google.protobuf.json_format import Parse
from google.protobuf.json_format import MessageToJson


try:
	def createAccount(contents):
		message = Parse(json.dumps(contents), ProtoDefination.CreateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		# print(jsonObj)

	def updateAccount(contents):
		my_list = ProtoDefination.UpdateAccount()
		message = Parse(json.dumps(contents), ProtoDefination.ActivateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		# print(jsonObj)


	def suSpendAccount(contents):
		my_list = ProtoDefination.SUSpendAccount()
		message = Parse(json.dumps(contents), ProtoDefination.ActivateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		# print(jsonObj)


	def activateAccount(contents):
		my_list = ProtoDefination.ActivateAccount()
		message = Parse(json.dumps(contents), ProtoDefination.ActivateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		print(jsonObj)

	def createSite(contents):
		my_list = ProtoDefination.CreateSite()
		message = Parse(json.dumps(contents), ProtoDefination.ActivateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		# print(jsonObj)


	def updateSite(contents):
		my_list = ProtoDefination.UpdateSite()
		message = Parse(json.dumps(contents), ProtoDefination.ActivateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		# print(jsonObj)


	def deleteSite(contents):
		my_list = ProtoDefination.DeleteSite()
		message = Parse(json.dumps(contents), ProtoDefination.ActivateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		# print(jsonObj)

	def createCredential(contents):
		my_list = ProtoDefination.CreateCredential()
		message = Parse(json.dumps(contents), ProtoDefination.ActivateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		# print(jsonObj)


	def updateCredential(contents):
		my_list = ProtoDefination.UpdateCredential()
		message = Parse(json.dumps(contents), ProtoDefination.ActivateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		# print(jsonObj)


	def regenerateCredential(contents):
		my_list = ProtoDefination.ListObjUse()
		message = Parse(json.dumps(contents), ProtoDefination.ActivateAccount())
		print("\n",base64.b64encode(message.SerializeToString()).decode(),"\n\n")

		jsonObj = MessageToJson(message)
		# print(jsonObj)


except Exception as error:
	import os,sys
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print("error----->",exc_type, fname, exc_tb.tb_lineno,error)



### calling function based on file name

with open(sys.argv[1], 'r') as f:
	contents = json.loads(f.read())

last_occurrence_index = sys.argv[1].rfind("/")
function_name = (sys.argv[1][last_occurrence_index+1:]).split(".",1)[0]

if function_name == "create_account":
	createAccount(contents)

if function_name == "update_account":
	updateAccount(contents)

if function_name == "su_spend_account":
	suSpendAccount(contents)

if function_name == "activate_account":
	activateAccount(contents)

if function_name == "create_site":
	createSite(contents)

if function_name == "update_site":
	updateSite(contents)

if function_name == "delete_site":
	deleteSite(contents)

if function_name == "create_credential":
	createCredential(contents)

if function_name == "update_credential":
	updateCredential(contents)

if function_name == "regenerate_credential":
	regenerateCredential(contents)
