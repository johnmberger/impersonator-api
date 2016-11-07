import os
from flask import Flask, jsonify, request
import markov
import praw

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'hello': 'This API scrapes reddit user comments and then generates a sentence based on those comments using NLP',
        'endpoint': 'https://impersonator.herokuapp.com/reddit/'
    })

@app.route('/reddit')
def reddit_instructions():
    return jsonify({
        'hello': 'add a reddit username to the url to generate a comment for that username. (usernames are case sensitive!)'
    })

@app.route('/reddit/<redditUsername>')
def get_comments(redditUsername):
    comments = ''
    r = praw.Reddit('markov_impersonator')
    user = r.get_redditor(redditUsername)
    try:
        for comment in user.get_comments(limit=250):
            comments = comments + ' ' + comment.body

        sentence = markov.makeSentence(comments)

        if comments == 'null':
            sentence = markov.makeSentence(comments)

        return jsonify({
        'reddit_username': redditUsername,
        'generated_sentence': sentence
        })
    except:
        return jsonify({"error": "username not found"})

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 404, 'message': 'This page does not exist'}), 404

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
