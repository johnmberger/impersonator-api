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

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
