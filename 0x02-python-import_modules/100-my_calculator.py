#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    out = sys.argv
    outLen = len(sys.argv)

    if outLen < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(out[1])
    b = int(out[3])

    add = add(a, b)
    sub = sub(a, b)
    mul = mul(a, b)
    div = div(a, b)

    if out[2] == '+':
        print("{} + {} = {}".format((a), (b), add))

    elif out[2] == '-':
        print("{} - {} = {}".format((a), (b), sub))
    elif out[2] == '*':
        print("{} * {} = {}".format((a), (b), mul))
    elif out[2] == '/':
        print("{} / {} = {}".format((a), (b), div))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
