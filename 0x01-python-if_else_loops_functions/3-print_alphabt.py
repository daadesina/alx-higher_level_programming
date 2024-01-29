#!/usr/bin/python3
num = range(97, 123)
for count in num:
    if count == 101:
        continue
    elif count == 113:
        continue
    out = chr(count)
    print("{}".format(out), end="")
