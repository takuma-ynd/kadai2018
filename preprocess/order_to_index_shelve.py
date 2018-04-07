import os
import sys
import shelve
from order_to_index import order_to_index


def order_to_index_shelve(src_file, shelve_file):
    word2idx = {}
    # (もし存在すれば)shelveファイルの内容をidx2wordにコピー
    if os.path.isfile(shelve_file):
        with shelve.open(shelve_file, "r") as f:
            for key, val in f.items():
                word2idx[key] = val
    # word2idxを更新
    word2idx = order_to_index(src_file, word2idx=word2idx)
    # 更新したword2idxをshelveファイルに保存
    with shelve.open(shelve_file) as f:
        for idx, word in word2idx.items():
            f[idx] = word

    return word2idx


if __name__ == "__main__":
    assert len(sys.argv) == 2
    shelve_file = "word2idx.db"
    order_to_index_shelve(sys.argv[1], shelve_file)
