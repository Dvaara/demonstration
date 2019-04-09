#!/usr/bin/env python

import os
import subprocess

from flask import Flask, flash, redirect, render_template, request, session, abort

# from flask import request
import json
import requests

import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

app = Flask(__name__)

opa_url = os.environ.get("OPA_ADDR", "http://localhost:8181")
policy_path = os.environ.get("POLICY_PATH", "/v1/data/httpapi/authz")
wso2_is = os.environ.get("WSO2_IS, wso2is")
salaries_endpoint = "http://backend:5003/finance/salary/bob"

def get_token(scopes):
    logging.info("Requesting an oauth2 token...")
    bashCommand = "./sslCurl2.sh https://wso2is:9443/oauth2/token grant_type=client_credentials"
    logging.info("Bach command:" + bashCommand)
    try:
        output = subprocess.check_output(['bash','-c', bashCommand])
        logging.info("SSLcURL:" + output);
        j=output
    except subprocess.CalledProcessError as e:
        logging.info("Token Response: {}".format(e.output))
        response = json.loads(e.output)
        j = response["access_token"]
    return j


def call_salary_api(token):
    resp = requests.get(salaries_endpoint, headers={"Authorization": "Bearer "+ token})
    if resp.status_code != 200:
        # This means something went wrong.
        logging.info("failed :" + resp)
        return "FAILED"
    return "SUCCEEDED"


@app.route('/', defaults={'path': ''}, methods = ['GET', 'POST', 'DELETE'])
@app.route('/<path:path>', methods = ['GET', 'POST'])
def root(path):
    j = get_token("clearance2")
    logging.info("Token response:" + j)
    response = call_salary_api(j)
    return render_template('index.html',name=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)