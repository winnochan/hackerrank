#!/usr/bin/env python

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    cSet = set([])

    aMap = {}
    for char in a:
        aMap.setdefault(char, 0)
        aMap[char] += 1
        cSet.add(char)

    bMap = {}
    for char in b:
        bMap.setdefault(char, 0)
        bMap[char] += 1
        cSet.add(char)

    count = 0
    for char in cSet:
        if char in aMap and char not in bMap:
            count += aMap[char]
        elif char in bMap and char not in aMap:
            count += bMap[char]
        else:
            count += abs(bMap[char] - aMap[char])
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # a, b = input(), input()

    a, b = 'fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    res = makeAnagram(a, b)

    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
