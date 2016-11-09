import markovify

def makeSentence(sentence):
    text_model = markovify.Text(sentence)
    return text_model.make_sentence()

def makeTweet(tweets):
    text_model = markovify.Text(tweets)
    return text_model.make_short_sentence(140)
