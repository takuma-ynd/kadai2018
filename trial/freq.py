import sys
assert len(sys.argv) == 2
d = {}
with open(sys.argv[1], "r") as f:
    for line in f:
        for word in line.strip().split():
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

# freq, alphabetical-orderの順に優先度が高いsortをする．
output = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for word, freq in output:
    print("".join((" " * 5, "{} {}".format(freq, word))))
