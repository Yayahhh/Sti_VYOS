#!/usr/bin/python

from flask import Flask, jsonify
from flask import abort, make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
from flask import request
auth = HTTPBasicAuth()

import dhcp

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

@app.route('/createdhcp', methods=['POST'])
@auth.login_required
def createdhcp():
    function = {
	'type' : request.json['type']
    }
    tasks.append(function)
    dhcp.createdhcp(function['type'])
    return jsonify({'dhcp': dhcp.readdhcp()})

@app.route('/readdhcp', methods=['GET'])
def readdhcp():
	return jsonify({'dhcp' : dhcp.readdhcp()})

@app.route('/deldhcp', methods=['POST'])
@auth.login_required
def deldhcp():
	function = {
		'type' : request.json['type']
	}
	tasks.append(function)
	dhcp.deldhcp(function['type'])
	return jsonify({'dhcp' : dhcp.readdhcp()})

@app.route('/updatedhcp', methods=['POST'])
@auth.login_required
def updatedhcp():
	function = {
		'type' : request.json['type'],
		'type1' : request.json['type1']
	}
	tasks.append(function)
	dhcp.updatedhcp(function['type'],function['type1'])
	return jsonify({'dhcp' : dhcp.readdhcp()})

if __name__ == '__main__':
	app.run(debug=True)

