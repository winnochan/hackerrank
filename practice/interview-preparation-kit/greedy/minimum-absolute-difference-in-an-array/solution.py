#!/usr/bin/env python

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    minAbs = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] < minAbs:
            minAbs = arr[i + 1] - arr[i]
    return minAbs


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(result)
