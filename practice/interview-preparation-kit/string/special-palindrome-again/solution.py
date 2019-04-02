#!/usr/bin/env python

import math
import os
import random
import re
import sys


def isSpecial(s):
    char = s[0]
    b, e = 0, len(s) - 1
    while b < e:
        if b < e:
            if s[b] != char or s[e] != char:
                return False
        b += 1
        e -= 1
    return True


# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    for i in range(n):
        c1, c2, w = i, i, 0
        while c1 - w >= 0 and c2 + w < len(s):
            c = s[c1 - w:c2 + w + 1]
            if isSpecial(c):
                count += 1
            else:
                break
            w += 1
        c1, c2, w = i, i + 1, 0
        while c1 - w >= 0 and c2 + w < len(s):
            c = s[c1 - w:c2 + w + 1]
            if isSpecial(c):
                count += 1
            else:
                break
            w += 1
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n, s = int(input()), input()

    n, s = 4, 'aaaa'

    result = substrCount(n, s)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
