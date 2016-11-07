from flask import Flask, jsonify, request
import markov
import praw

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({
        'hi': 'Hello World!'
    })

@app.route('/<word>')
def hello_hell(word):
    return jsonify({"url param": word})

@app.route('/reddit/<redditUsername>')
def get_comments(redditUsername):
    comments = ''
    r = praw.Reddit('markov_impersonator')
    user = r.get_redditor(redditUsername)
    for comment in user.get_comments(limit=250):
        comments = comments + ' ' + comment.body

    sentence = markov.makeSentence(comments)
    if sentence == 'null':
        sentence = markov.makeSentence(comments)
    return jsonify({"sentence": sentence})
