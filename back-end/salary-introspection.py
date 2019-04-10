#!/usr/bin/env python

import base64
import os
import subprocess

from flask import Flask
from flask import request
from flask import Response
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

# @cached(cache)
def check_auth(url, user, method, user_agent, remote_addr, token):
    headers = "dummy#value@method#"+method+"@user_agent#"+user_agent+"@remote_addr#"+remote_addr+"@resource#"+url+"@user#"+user

    logging.info("Checking auth...")
    logging.info(json.dumps(headers, indent=2))
    bashCommand = "./sslCurl2.sh https://wso2is:9443/oauth2/introspect token="+token+" headers="+headers;
    try:
        output = subprocess.check_output(['bash','-c', bashCommand])
        logging.info("SSLcURL:" + output)
    except subprocess.CalledProcessError as e:
        logging.info("command '{}' return with response (code {}): {}".format(e.cmd, e.returncode, e.output))
        j =json.loads(e.output)
        response = j['active']
        logging.info(response)
    return response

@app.route('/finance/salary/<username>', methods = ['GET', 'POST', 'DELETE'])
def root(username):
    # user_encoded = request.headers.get('Authorization', "Anonymous:none")
    logging.info("User Agent: %s" % request.user_agent.string)
    logging.info("Remote Address: %s" % request.remote_addr)
    logging.info("OAuth2.0 token: %s" % request.headers.get("Authorization"))
    logging.info("Endpoint"+request.full_path)
    logging.info("Args" + username)
    logging.info("Method" + request.method)
    if request.headers.get("Authorization"):
        token = request.headers.get("Authorization").split("Bearer ")[1]
    # user = request.view_args["username"]
    url = request.full_path.replace("?","")
    # path_as_array = path.split("/")
    j = check_auth(url, username, request.method, request.user_agent.string, request.remote_addr, token)
    if not j:
        return Response("{'allow':'no'}", status=401, mimetype='application/json')
    return Response("{'allow':'yes'}", status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)