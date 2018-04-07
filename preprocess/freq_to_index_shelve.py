import sys
import shelve
from freq_nltk import file_to_freqdict
from freq_to_index import freq_to_index

word2idx = freq_to_index(file_to_freqdict(sys.argv[1]))
with shelve.open('word_to_idx.db') as f:
    for key, val in word2idx.items():
        f[key] = val
