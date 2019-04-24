#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c = sorted(c, reverse=True)

    s = 0
    for i in range(len(c)):
        price = c[i]
        pre = i // k
        s += (1 + pre) * price

    return s


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, k = map(int, input().strip().split())

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(minimumCost)

    # fptr.write(str(minimumCost) + '\n')

    # fptr.close()
