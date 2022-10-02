#!/opt/bb/bin/python3.9

def summ(x, y):
    return x+y


def check_this(a, b):
    return a * b


if __name__ == "__main__":
    ss = summ(5, 10)
    print(f"Sum is {ss}")
    mult = check_this(5, 10)
    print(f"Mult is {mult}")
    