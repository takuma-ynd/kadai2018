import sys
import re
assert len(sys.argv) == 3
p = re.compile(sys.argv[1])
with open(sys.argv[2], "r") as f:
    for line in f:
        if p.search(line) is not None:
            print(line, end="")
