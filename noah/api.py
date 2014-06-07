from flask import Flask, jsonify
from noah import Noah

api = Flask(__name__)

with open('../dictionaries/english.json') as dictionary:
    n = Noah(dictionary)

base_url = '/noah/api/'
version = 'v0.1'
api_base = base_url + version

@api.route(api_base)
def index():
    return 'Noah'

@api.route(api_base + '/list', methods=['GET'])
def list():
	return jsonify({ 'response': n.list() })

@api.route(api_base + '/list/<string:query>', methods=['GET'])
def list_filter(query):
	return jsonify({ 'response': n.list_filter(query) })

@api.route(api_base + '/define/<string:word>', methods=['GET'])
def define(word):
	return jsonify({ 'response': n.define(word) })

@api.route(api_base + '/random', methods=['GET'])
def random():
    return jsonify({ 'response': n.random() })

if __name__ == '__main__':
    api.run(debug=True)