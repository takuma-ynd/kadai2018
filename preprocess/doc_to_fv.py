import sys
from order_to_index_shelve import order_to_index_shelve
from freq_nltk import file_to_freqdict


def doc_to_fv(file_name, shelve_file):
    word2freq = file_to_freqdict(file_name)
    word2idx = order_to_index_shelve(file_name, shelve_file)
    idx2freq = {}
    for word, freq in word2freq.items():
        idx2freq[word2idx[word]] = freq
    return idx2freq


def repr_fv(idx2freq):
    return " ".join(":".join((str(idx), str(freq))) for idx, freq in sorted(idx2freq.items(), key=lambda x: x[0]))


if __name__ == "__main__":
    assert len(sys.argv) == 2
    shelve_file = "word2idx.db"
    idx2freq = doc_to_fv(sys.argv[1], shelve_file)
    fv = repr_fv(idx2freq)
    print(fv)
