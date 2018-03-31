import sys
assert len(sys.argv) == 2
with open(sys.argv[1]) as f:
    for line in f:
        words = line.strip().split()
        for word in words:
            print(word)
