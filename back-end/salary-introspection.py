#!/usr/bin/env python

import base64
import os
import subprocess

from flask import Flask
from flask import request
import json
import requests
from cachetools import cached, TTLCache

import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

app = Flask(__name__)

cache = TTLCache(maxsize=100, ttl=300)
opa_url = os.environ.get("OPA_ADDR", "http://localhost:8181")
policy_path = os.environ.get("POLICY_PATH", "/v1/data/httpapi/authz")

@cached(cache)
def check_auth(url, user, method, user_agent, remote_addr,url_as_array, token):
    input_dict = {"input": {
        "user": user,
        "path": url_as_array,
        "method": method,
	    "user_agent": user_agent,
	    "remote_addr": remote_addr,
        "resource" : url
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

@app.route('/finance/salary/<username>', defaults={'path': ''}, methods = ['GET', 'POST', 'DELETE'])
@app.route('/<path:path>', methods = ['GET', 'POST'])
def root(path, username):
    # user_encoded = request.headers.get('Authorization', "Anonymous:none")
    logging.info("User Agent: %s" % request.user_agent.string)
    logging.info("Remote Address: %s" % request.remote_addr)
    logging.info("OAuth2.0 token: %s" % request.headers.get("Authorization"))
    logging.info("Endpoint"+request.full_path)
    logging.info("Args" + username)
    if request.headers.get("Authorization"):
        token = request.headers.get("Authorization").split("Bearer ")[1]
    user = request.view_args["username"]
    url = request.full_path.replace("?","")
    # path_as_array = path.split("/")
    j = check_auth(url, user, request.method, request.user_agent.string, request.remote_addr, path, token)
    if not j:
        return "Error: user %s is not authorized to %s url /%s \n" % (user, request.method, path)
    return "Success: user %s is authorized \n" % user

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)