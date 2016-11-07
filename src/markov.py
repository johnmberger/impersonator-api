import markovify

def makeSentence(sentence):
    text_model = markovify.Text(sentence)
    return text_model.make_sentence()
