from flask import Flask, jsonify
from noah import Noah

app = Flask(__name__)

with open('../dictionaries/english.json') as dictionary:
    n = Noah(dictionary)

@app.route('/')
def index():
    return 'Noah'

@app.route('/noah/api/v0.1/list', methods=['GET'])
def list():
	return jsonify({ 'response': n.list() })

@app.route('/noah/api/v0.1/define/<string:word>', methods=['GET'])
def define(word):
	return jsonify({ 'response': n.define(word) })

@app.route('/noah/api/v0.1/random', methods=['GET'])
def random():
    return jsonify({ 'response': n.random() })

if __name__ == '__main__':
    app.run(debug=True)