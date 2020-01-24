#!/usr/bin/env python

import math
import os
import random
import re
import sys


# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):

    charPosMap = {}

    for i in range(len(s)):
        c = s[i]
        charPosMap.setdefault(c, [])
        charPosMap[c].append(i)

    for c in charPosMap:
        charPosMap[c].sort()

    charList = sorted(charPosMap.keys())

    first = charList[0]
    chooseMap = {}
    chooseMap[first] = charPosMap[first][len(charPosMap[first]) // 2:]

    for i in range(1, len(charList)):
        l = charList[i + 1]

    print(charPosMap)
    print(chooseMap)
    # print(reverseCharList)
    # print(charCountMap, passedMap, chooseMap, reverseCharList)

    # return ''.join(reverseCharList)
    return


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
