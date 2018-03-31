# 2.3 英語レビューの Python を利用した解析 (1)

## 2.4
```sample code
$ diff <(python3 cat_cv000.py) <(cat hogehoge.txt)
```

## 2.5
```
$ diff <(python3 cat_cv000.py hogehoge.txt) <(cat hogehoge.txt)
```

## 2.7
(可能なら)正規表現が使えるようにコードを書くこと． ( re module )
## 2.9
```
$ uniq -c file
```
の出力形式を od コマンド等で確認しておくと良いかもしれない．  
どうやら
```
spc spc spc spc freq spc word \n
```
となっているみたい．

## 2.10
[スライド](https://docs.google.com/presentation/d/1-UpuAV0LvWwQw5JETuEvT7cwSeMM01nIOChSAqGo64I/edit?usp=sharing)参照