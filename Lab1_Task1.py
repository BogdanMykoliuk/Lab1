import argparse

parser = argparse.ArgumentParser()
parser.add_argument("first", type=str)
parser.add_argument("second", type=str)
parser.add_argument("third", type=str)
args = parser.parse_args()

# receive arguments from command line
if args.first.isdigit() and args.third.isdigit():
    if args.second == "+" or args.second == "-" or args.second == "*":
        print("Result is:", eval(args.first + args.second + args.third))
    elif args.second == "/" and args.third == "0":
        print("Division by zero")
    else:
        print(eval(args.first + args.second + args.third))
else:
    print("Error")
# sum string and convert them to int and count result
