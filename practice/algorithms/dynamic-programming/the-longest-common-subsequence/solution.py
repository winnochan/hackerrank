#!/usr/bin/env python

import math
import os
import random
import re
import sys
from pprint import pprint


# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    arr = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])

    charMap = {}
    l, charList = 0, []
    for i in range(1, len(b) + 1):
        if arr[len(a)][i] > l:
            charMap[l] = b[i - 1]
            l = arr[len(a)][i]
            # charList.append()
    # return arr[i][j]
    # print(charMap, l)
    # return charList
    return [charMap[i] for i in range(l)]


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)
    print(len(result))
    # print(
    #     ' '.join(map(str, result)) ==
    #     '438 591 160 894 782 445 326 452 7 544 12 347 828 336 692 339 130 837 989 875 711 957 338 328 7 670 328 699 668 609 322 386 635 952 618 73 221 398 579 660 746 718 918 224 242 506 734 324 100 346 532 914 130'
    # )
    print(
        len('438 591 160 894 782 445 326 452 7 544 12 347 828 336 692 339 130 837 989 875 711 957 338 328 7 670 328 699 668 609 322 386 635 952 618 73 221 398 579 660 746 718 918 224 242 506 734 324 100 346 532 914 130'
            .split()))

    print(result)
