#!/usr/bin/python

from flask import Flask, jsonify
from flask import abort, make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
from flask import request
auth = HTTPBasicAuth()

import interface

app = Flask(__name__)

tasks = [
    {

    }
]

@auth.get_password
def get_password(username):
    if username == 'yayah':
        return 'Passw0rd!'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/createinterface', methods=['POST'])
@auth.login_required
def createinterface():
        function = {
                'eth1' : request.json['eth1'],
                'desc1' : request.json['desc1'],
		'ip1' : request.json['ip1']
        }
        tasks.append(function)
        interface.createinterface(function['eth1'],function['ip1'],function['desc1'])
        return jsonify({'interface' : interface.readinterface()})

@app.route('/readinterface', methods=['GET'])
def readinterface():
        return jsonify({'interface' : interface.readinterface()})

@app.route('/delinterface', methods=['POST'])
@auth.login_required
def delinterface():
        function = {
                'eth' : request.json['eth']
        }
        tasks.append(function)
        interface.delinterface(function['eth'])
        return jsonify({'interface' : interface.readinterface()})

@app.route('/updateinterface', methods=['POST'])
@auth.login_required
def updateinterface():
        function = {
		'eth' : request.json['eth'],
                'eth1' : request.json['eth1'],
                'desc1' : request.json['desc1'],
		'ip1' : request.json['ip1']
        }
        tasks.append(function)
        interface.updateinterface(function['eth'],function['eth1'],function['ip1'],function['desc1'])
        return jsonify({'interface' : interface.readinterface()})

if __name__ == '__main__':
    app.run(debug=True)

