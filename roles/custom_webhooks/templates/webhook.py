from flask import Flask, jsonify
from flask import request
import json, hashlib, hmac, os
import subprocess as sp
app = Flask(__name__)

secret = os.environ['secretFile']
pipelineScript = os.environ['pipelineScript']

def getSignature(message, secret):
	""" Returns sha1 HMAC of the message, using the secret """
	return 'sha1=' + hmac.new(secret, message, hashlib.sha1).hexdigest()

@app.route("/", methods=['GET'])
def hello():
    return "App only responds to POST methods from Github"

@app.route('/', methods=['POST'])
def handleHook():
	if request.is_json:
		sig = request.headers.get('X-Hub-Signature')
		localSig = getSignature(request.get_data(), secret)
		if sig == localSig:
		#	retCode = sp.call(pipelineScript)
			return 'Received event'
		else:
			return 'The signature ({0}) did not match our secret ({1}). Exiting now!'.format(
				sig, localSig)
	else:
		return 'This needs to be json..'
