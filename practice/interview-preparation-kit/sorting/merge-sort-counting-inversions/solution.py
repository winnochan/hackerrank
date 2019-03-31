#!/usr/bin/env python

import math
import os
import random
import re
import sys


# Complete the countInversions function below.
def merge(arr, b, w):
    e = b + w
    m = (b + e) // 2
    c = 0
    tmp = []

    # print(arr, b, m, e)

    j, k = b, m
    while j < m and k < e and k < len(arr):
        if arr[j] <= arr[k]:
            tmp.append(arr[j])
            j += 1
        else:
            tmp.append(arr[k])
            k += 1
            c += k - b - len(tmp)
    if j == m:
        tmp.extend(arr[k:e])
    elif k == e or k == len(arr):
        tmp.extend(arr[j:m])

    for i in range(len(tmp)):
        arr[b + i] = tmp[i]

    # print(arr, tmp, c)
    return c


def countInversions(arr):
    c, w, l = 0, 2, len(arr)
    while w // 2 <= l:
        for i in range(0, l, w):
            c += merge(arr, i, w)
        w *= 2
    # print(arr)
    return c


if __name__ == '__main__':
    # arr = list(map(int, '7 5 3 1'.rstrip().split()))
    # arr = list(map(int, '1 1 1 2 2'.rstrip().split()))
    # arr = list(map(int, '2 1 3 1 2'.rstrip().split()))
    # result = countInversions(arr)
    # print(result)
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(result)
