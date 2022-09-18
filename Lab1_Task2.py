import argparse

parser = argparse.ArgumentParser()
parser.add_argument("first", type=str)
parser.add_argument("second", type=str)
parser.add_argument("third", type=str)
args = parser.parse_args()

# receive arguments from command line
if args.second.isdigit() and args.third.isdigit():
    if args.first == "add":
        print("Result is:", int(args.second) + int(args.third))
    elif args.first == "mul":
        print("Result is:", int(args.second) * int(args.third))

    elif args.first == "sub":
        print("Result is:", int(args.second) - int(args.third))

    elif args.first == "div":
        if args.third == "0":
            print("division by zero")
        else:
            print(" Result is:", int(args.second) / int(args.third))

    else:
        print("Unknown function")

else:
    print("No numbers!")

