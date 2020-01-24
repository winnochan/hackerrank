#!/usr/bin/env python

import math
import os
import random
import re
import sys
"""
f(b, c) = max(arr[b] + f(b + 2, c + 1), f(b + 1, c))
        = max(arr[b] + f(b + 2, c + 1), max(f()))
"""


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr, b=0, c=0, cache={}):
    c = (len(arr) + 1) // 2

    if b >= len(arr):
        return 0 if c >= 2 else -10001

    # cache = {}

    # for n in arr:
    #     if

    if (b, c) in cache:
        return cache[(b, c)]

    cache[(b, c)] = max(arr[b] + maxSubsetSum(arr, b + 2, c + 1, cache),
                        maxSubsetSum(arr, b + 1, c, cache))
    return cache[(b, c)]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
