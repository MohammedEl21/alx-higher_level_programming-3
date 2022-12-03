#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as c
    import sys

    operator = {
        "add": "+",
        "sub": "-",
        "mul": "*",
        "div": "/"
    }

    args = len(sys.argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if sys.argv[1].isdigit() and sys.argv[3].isdigit():
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == operator.get("add"):
            print("{} + {} = {}".format(a, b, c.add(a, b)))
        elif sys.argv[2] == operator.get("sub"):
            print("{} - {} = {}".format(a, b, c.sub(a, b)))
        elif sys.argv[2] == operator.get("mul"):
            print("{} * {} = {}".format(a, b, c.mul(a, b)))
        elif sys.argv[2] == operator.get("div"):
            print("{} / {} = {:.2f}".format(a, b, c.div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
