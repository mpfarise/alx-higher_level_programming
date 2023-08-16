#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arthimetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) -1 != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator == "/" and b == 0:
        print("Cannot divide by zero.")
        sys.exit(1)

    result = ops[operator]{a, b)
    print("{} {} {} = {}".format(a, operator, b, result)
