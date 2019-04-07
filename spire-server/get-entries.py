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

def check_entries():
    logging.info("Getting Entries from SPIRE server...")
    bashCommand = "./get-entries.sh";
    try:
        output = subprocess.check_output(['bash','-c', bashCommand])
        logging.info("entries:" + output);
        response = output
    except subprocess.CalledProcessError as e:
        logging.info("command '{}' return with response (code {}): {}".format(e.cmd, e.returncode, e.output))
        j =json.loads(e.output);
        response = j['active']
        logging.info(response)
    return response

@app.route('/', defaults={'path': ''}, methods = ['GET'])
@app.route('/<path:path>', methods = ['GET', 'POST'])
def root(path):
    logging.info("User Agent: %s" % request.user_agent.string)
    logging.info("Remote Address: %s" % request.remote_addr)
    j = check_entries()
    if not j:
        return "Error: Could not retrieve entries"
    return "Success: found entries %s  \n" % j

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)