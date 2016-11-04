from flask import Flask, jsonify
import test

app = Flask(__name__)
fromAnother = test.other()

@app.route('/')
def hello_world():
    return jsonify({
    'Message': fromAnother,
    'Other Message': 'Hi'
    })
