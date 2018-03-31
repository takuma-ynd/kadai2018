# 2.2 英語レビューの取得・処理の準備

## 2.2.6
### man wc
Print  newline,  word, and byte counts for each FILE.
The options may be used to select which counts are printed, always in the following order: newline, word, character, byte, maximum line length.

```sample code
wc *
```

### 2.2.8
### man grep
-w: Select only those lines containing matches that form whole words.
-c: Suppress normal output; instead print a count of matching lines for each input file.
-i: Ignore case distinctions in both the PATTERN and the input files.
-o: Print only the matched (non-empty) parts of a matching line, with each such part on a separate output line.
```sample code
;; 文字列theを含む文の数('theory', 'breathe'などを含む行を含む．)．
grep -c the hogehoge.txt

;; 単語theを含む文の数．
grep -wc the hogehoge.txt

;; 単語theの数
cat hogehoge.txt | grep -ow the | wc -l
```
