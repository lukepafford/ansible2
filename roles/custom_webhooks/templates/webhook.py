from flask import Flask, jsonify
from flask import request
from task_queue import runFlaskPipeline
import json, hashlib, hmac, os
import subprocess as sp
app = Flask(__name__)

secret = os.environ['secretFile'].encode()
pipelineScript = os.environ['pipelineScript']

def getSignature(secret, message):
	""" Returns sha1 HMAC of the message, using the secret """
	return 'sha1=' + hmac.new(secret, message, hashlib.sha1).hexdigest()

@app.route("/", methods=['GET'])
def hello():
    return "App only responds to POST methods from Github"

@app.route('/', methods=['POST'])
def handleHook():
	sig = request.headers.get('X-Hub-Signature')
	localSig = getSignature(secret, request.get_data())
	# WARNING
	# For the life of me, I don't know how github creates their
	# HMAC signaturees. The secrets are the same, but the hmac always
	# differs. I am not doing verification right now and this is a big
	# security issue I'll need to figure out
	#if sig == localSig:
	if sig:
		res = runFlaskPipeline.delay()
		if res.status in [ 'PENDING', 'SUCCESS', 'STARTED']:
			return 'Received event and scheduled pipeline'
		else:
			return 'Something went wrong with task {0}'.format(res)
	else:
		return 'Request did not contain proper headers...'
