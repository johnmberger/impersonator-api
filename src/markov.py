import markovify

with open("src/corpora/science.txt", encoding = "ISO-8859-1") as f:
    text = f.read()

text_model = markovify.Text(text)

def makeSentence():
    return text_model.make_sentence()
