import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", nargs='+', type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()


def maxweight(W, w):
    """
    Function, which find maximum weight which can be stored in rucksack
    """
    w = [0] + w
    items = len(w)
    capacity = W + 1
    matrix = [[0 for i in range(items)] for i in range(capacity)]

    for i in range(1, items):
        for j in range(1, capacity):
            matrix[j][i] = matrix[j][i - 1]
            if w[i] <= j:
                val = matrix[j - w[i]][i - 1] + w[i]
                if matrix[j][i] < val:
                    matrix[j][i] = val
    return matrix[-1][-1]

    # read capacity, number of bars and weight of every bar


print(maxweight(args.W, args.w))
