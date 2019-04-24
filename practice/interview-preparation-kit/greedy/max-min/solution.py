#!/usr/bin/env python

import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr):
    arr = sorted(arr)

    ret = arr[k - 1] - arr[0]
    for i in range(1, len(arr) + 1 - k):
        if arr[k + i - 1] - arr[i] < ret:
            ret = arr[k + i - 1] - arr[i]

    return ret


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = [int(input()) for _ in range(n)]

    result = maxMin(k, arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
