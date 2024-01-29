#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    out = sys.argv
    outLen = range(1, len(sys.argv))
    myOut = 0

    for i in outLen:
        myOut = myOut + int(out[i])

    print(myOut)
