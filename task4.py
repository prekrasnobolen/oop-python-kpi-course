# Task #04
# You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
# There is only one instance of each bar and for each bar you can either take it or not (hence you cannot take a
# fraction of a bar).
# Write a function that returns the maximum weight of gold that fits into a knapsack's capacity.
# The first parameter contains 'capacity' - integer describing the capacity of a knapsack.
# The next parameter contains 'weights' - list of weights of each gold bar.
# The last parameter contains 'bars_number' - integer describing the number of gold bars.
# Output : Maximum weight of gold that fits into a knapsack with capacity of W.
# Note:
# Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
# Example of how the task should be called:
# $ python task3_1.py -W 56 -w 3 4 5 6 -n 4
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", "--Weight", type=int, required=True, help="Maximum weight")
parser.add_argument("-w", "--weights", type=int, nargs="+", help="Weights of gold bars")
parser.add_argument("-n", "--number", type=int, help="Number of gold bars")
args = parser.parse_args()


def stolenButUnderstoodDP(W, val, n):
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif val[i - 1] <= j:
                table[i][j] = max(val[i - 1]
                                  + table[i - 1][j - val[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    return table[n][W]

print(stolenButUnderstoodDP(args.Weight, args.weights, args.weights))
