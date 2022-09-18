import argparse

parser = argparse.ArgumentParser()
parser.add_argument("first", type=str)
args = parser.parse_args()


def check(first):
    string = first
    for i in range(len(first) + 1):
        if len(first) == 0:
            solving(string)
            break
        elif first[-1] == "+" or first[-1] == "-" or first[-1] == "*" or first[-1] == "/":
            error()
            break
        elif first[0] == "/":
            if first[1] == "0":
                error()
                break
            else:
                first = first[1:]
        elif first[0] == "+" or first[0] == "-" or first[0] == "*" or first[0] == "/":
            if first[1] == "+" or first[1] == "-" or first[1] == "*" or first[1] == "/":
                error()
                break
            else:
                first = first[1:]

        elif first[0].isdigit():
            first = first[1:]
        else:

            error()
            break


def solving(first):
    print("True,", eval(first))


def error():
    print("False, None")


check(args.first)
