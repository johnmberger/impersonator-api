from flask import Flask, jsonify
import test
import markov
import bot

app = Flask(__name__)

fromAnother = test.other()
blob = bot.getBlob()
sentence = markov.makeSentence()

@app.route('/')
def hello_world():
    return jsonify({
        'Message': fromAnother,
        'Sentence': sentence,
        'blob': blob
    })
