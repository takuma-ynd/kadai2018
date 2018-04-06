import sys
from nltk.tokenize import sent_tokenize, word_tokenize

with open(sys.argv[1], 'r') as f:
    text = f.read()
sentences = sent_tokenize(text)
words = []
for sentence in sentences:
    words.extend(word_tokenize(sentence))

for e in words:
    print(e)
