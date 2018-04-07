import sys
from word_tokenize import word_tokenize_file


def order_to_index(file_name, word2idx={}):
    """単語の出現順にインデックス付けを行う"""
    words = word_tokenize_file(file_name)
    for word in words:
        if word not in word2idx:
            word2idx[word] = len(word2idx) + 1
    return word2idx


if __name__ == "__main__":
    assert len(sys.argv) == 2
    word2idx = order_to_index(sys.argv[1])
    for word, idx in sorted(word2idx.items(), key=lambda x: x[1]):
            print("".join((" " * 5, "{} {}".format(idx, word))))
