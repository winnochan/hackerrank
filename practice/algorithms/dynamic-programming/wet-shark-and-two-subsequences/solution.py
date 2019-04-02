#!/usr/bin/env python

import os
import sys
from itertools import combinations


def twoSubsequences(x, r, s):
    m, a, b, c = len(x), (r + s) // 2, (r - s) // 2, 0

    # print(m, a, b, n)

    allSums = {}
    for i in range(m):
        c1 = combinations(x, i + 1)
        # print(list(c1))
        for c2 in combinations(c1, 2):
            # print(list(c2))
            if c2[0] in allSums:
                s0 = allSums[c2[0]]
            else:
                s0 = allSums[c2[0]] = sum(c2[0])
            if c2[1] in allSums:
                s1 = allSums[c2[1]]
            else:
                s1 = allSums[c2[1]] = sum(c2[1])
            if (s0 == a and s1 == b) or (s0 == b and s1 == a):
                c += 1

    return c % 1000000007


if __name__ == '__main__':
    m, r, s = map(int, input().strip().split())
    x = list(map(int, input().rstrip().split()))

    # m, r, s, x = 4, 5, 3, [1, 1, 1, 4]

    result = twoSubsequences(x, r, s)

    print(result)
