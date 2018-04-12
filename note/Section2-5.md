# 2.5 分類機の作成・利用

## 2.5.2
```bash
$ cat <(cat pos_data.txt | head -n 800) <(cat neg_data.txt | head -n 800) > train.txt
$ cat <(sed -n 801,900p pos_data.txt) <(sed -n 801,900p neg_data.txt) > devel.txt
$ cat <(sed -n 901,1000p pos_data.txt) <(sed -n 901,1000p neg_data.txt) > test.txt
```

