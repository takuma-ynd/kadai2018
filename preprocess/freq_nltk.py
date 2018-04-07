import sys
from word_tokenize import word_tokenize_file


def file_to_freqdict(file_name):
    words = word_tokenize_file(file_name)
    word2freq = {}
    for word in words:
        if word in word2freq:
            word2freq[word] += 1
        else:
            word2freq[word] = 1
    return word2freq


if __name__ == "__main__":
    assert len(sys.argv) == 2
    word2freq = file_to_freqdict(sys.argv[1])
    output = sorted(word2freq.items(), key=lambda x: (-x[1], x[0]))
    for word, freq in output:
            print("".join((" " * 5, "{} {}".format(freq, word))))
