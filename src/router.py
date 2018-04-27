import os
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import markov
import praw

import twitter
api = twitter.Api(consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='')

app = Flask(__name__)

CORS(app)

@app.route('/')
def hello_world():
    return jsonify({
        'hello': 'This API scrapes reddit user comments and then generates a sentence based on those comments using NLP',
        'endpoint': 'https://impersonator.herokuapp.com/reddit'
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

        return jsonify({
        'reddit_username': redditUsername,
        'generated_sentence': sentence
        })

    except:
        return jsonify({"error": "username not found"}), 404

@app.route('/twitter')
def reddit_instructions():
    return jsonify({
        'hello': 'add a twitter handle to the url to generate a tweet for that username.'
    })

@app.route('/twitter/<twitterHandle>')
def get_tweets(twitterHandle):
    new_tweets = api.GetUserTimeline(screen_name=twitterHandle)

    try:
        tweets = ''
        for tweet in new_tweets:
            tweets = tweets + ' ' + tweet.text

        tweet = markov.makeTweet(tweets)
        return jsonify({'tweet': tweet})

    except:
        return jsonify({"error": "something went wrong"}), 404

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'error': 404, 'message': 'This page does not exist'}), 404

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
