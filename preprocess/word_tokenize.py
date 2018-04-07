import sys
from nltk.tokenize import sent_tokenize, word_tokenize


def word_tokenize_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    sentences = sent_tokenize(text)
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))
    return words


if __name__ == "__main__":
    assert len(sys.argv) == 2
    words = word_tokenize_file(sys.argv[1])
    for e in words:
        print(e)
