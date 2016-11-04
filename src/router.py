from flask import Flask, jsonify
import test
import bot

app = Flask(__name__)

fromAnother = test.other()
blob = bot.getBlob()

@app.route('/')
def hello_world():
    return jsonify({
        'Message': fromAnother,
        'Other Message': 'Hi',
        'TextBlob': blob
    })
