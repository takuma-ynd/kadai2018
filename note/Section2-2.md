# 2.2 英語レビューの取得・処理の準備
## 2.2.6
### wc (word, line, character, and byte count)
* Print  newline,  word, and byte counts for each FILE.
* The options may be used to select which counts are printed, always in the following order: newline, word, character, byte, maximum line length.

```sample code
# カレントディレクトリの全ファイルに対し，行数・単語数・バイト数をカウント
$ wc *
```

## 2.2.8
### grep
* **-w** Select only those lines containing matches that form whole words.
* **-c** Suppress normal output; instead print a count of matching lines for each input file.
* **-i** Ignore case distinctions in both the PATTERN and the input files.
* **-o** Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line.

```sample code
# 文字列theを含む文の数('theory', 'breathe'などを含む行を含む)をカウント
$ grep -c the hogehoge.txt

# 単語theを含む文の数をカウント
$ grep -wc the hogehoge.txt

# 単語theの数をカウント
$ cat hogehoge.txt | grep -ow the | wc -l
```

## 2.2.9
### sed (stream editor)

* [sedとは](https://hwb.ecc.u-tokyo.ac.jp/current/applications/textprocessing/sed/)
* [Qiita: sedのパターンスペース・ホールドスペースの動作を図で学ぶ](https://qiita.com/gin_135/items/773fec1343a69c9f90d6)
* [StackOverFlow: How can I replace a newline (\n) using sed?
](https://stackoverflow.com/questions/1251999/how-can-i-replace-a-newline-n-using-sed)

```sample code
# ファイルに含まれる全ての改行(\n)を削除
$ cat hogehgoe.txt | tr -d "\n"
$ sed -z "s/\n//g" hogehoge.txt

# ファイルに含まれる全ての改行(\n)を削除し，空白を改行(\n)に置換
$ cat hogehoge.txt | tr -d "\n" | sed "s/ /\n/g"
$ sed -ze 's/\n//g' -e 's/ /\n/g' hogehoge.txt
```

## 2.2.10
### uniq
* **-c** prefix lines by the number of occurrences

```sample code
$ cat hogehoge.txt | tr -d "\n" | sed "s/ /\n/g" | sort | uniq -c | sort -r | head -n 10 > top10.txt
$ cat hogehoge.txt | tr -d "\n" | sed "s/ /\n/g" | sort | uniq -c | sort -r | tail -n 10 > low10.txt
```
