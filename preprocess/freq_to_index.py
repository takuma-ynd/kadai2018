import sys
from freq_nltk import file_to_freqdict


def freq_to_index(word2freq):
    word2idx = {}
    for word, _ in sorted(word2freq.items(), key=lambda x: (x[-1], x[0])):
        if word not in word2idx:
            word2idx[word] = len(word2idx) + 1
    return word2idx


if __name__ == "__main__":
    assert len(sys.argv) == 2
    word2idx = freq_to_index(file_to_freqdict(sys.argv[1]))
    for idx, word in sorted(word2idx.items(), key=lambda x: -x[1]):
            print("".join((" " * 5, "{} {}".format(idx, word))))
