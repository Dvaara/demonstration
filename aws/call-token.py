#!/usr/bin/env python

import base64
import os
import subprocess

from flask import Flask
from flask import request
import json
import requests

import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

app = Flask(__name__)

opa_url = os.environ.get("OPA_ADDR", "http://localhost:8181")
policy_path = os.environ.get("POLICY_PATH", "/v1/data/httpapi/authz")

def check_auth(url, user, method, user_agent, remote_addr,url_as_array, token):
    input_dict = {"input": {
        "user": user,
        "path": url_as_array,
        "method": method,
	    "user_agent": user_agent,
	    "remote_addr": remote_addr
    }}
    if token is not None:
        input_dict["input"]["token"] = token

    logging.info("Checking auth...")
    logging.info(json.dumps(input_dict, indent=2))
    bashCommand = "./sslCurl2.sh https://wso2is:9443/oauth2/introspect token="+token;
    try:
        output = subprocess.check_output(['bash','-c', bashCommand])
        logging.info("SSLcURL:" + output);
    except subprocess.CalledProcessError as e:
        logging.info("command '{}' return with response (code {}): {}".format(e.cmd, e.returncode, e.output))
        j =json.loads(e.output);
        response = j['active']
        logging.info(response)
    return response

@app.route('/', defaults={'path': ''}, methods = ['GET', 'POST', 'DELETE'])
@app.route('/<path:path>', methods = ['GET', 'POST'])
def root(path):
    user_encoded = request.headers.get('Authorization', "Anonymous:none")
    logging.info("User Agent: %s" % request.user_agent.string)
    logging.info("Remote Address: %s" % request.remote_addr)
    if user_encoded:
        user_encoded = user_encoded.split("Basic ")[1]
    user, _ = base64.b64decode(user_encoded).decode("utf-8").split(":")
    url = opa_url + policy_path
    path_as_array = path.split("/")
    token = request.args["token"] if "token" in request.args else None
    j = check_auth(url, user, request.method, request.user_agent.string, request.remote_addr, path_as_array, token)
    if not j:
        return "Error: user %s is not authorized to %s url /%s \n" % (user, request.method, path)
    return "Success: user %s is authorized \n" % user

if __name__ == "__main__":
    app.run()