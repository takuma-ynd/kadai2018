import sys
assert len(sys.argv) == 2
with open(sys.argv[1]) as f_src:
    src_text = f_src.read()
    with open(sys.argv[2]) as f_tar:
        f_tar.write(src_text)
