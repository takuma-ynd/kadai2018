import sys
from nltk.tokenize import sent_tokenize

with open(sys.argv[1], 'r') as f:
    text = f.read()
    sentences = sent_tokenize(text)

for e in sentences:
    print(e)
