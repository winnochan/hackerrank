#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the commonChild function below.


def commonChild(s1, s2):
    # commonChars = set(s1) & set(s2)
    # s1 = ''.join(filter(lambda c: c in commonChars, list(s1)))
    # s2 = ''.join(filter(lambda c: c in commonChars, list(s2)))
    s1 = '!' + s1
    s2 = '!' + s2
    l1, l2 = len(s1) - 1, len(s2) - 1
    table = [[0 for _ in s2] for _ in s1]
    # print(table)

    for i1 in range(1, len(s1)):
        for i2 in range(1, len(s2)):
            if table[i1][i2]:
                continue
            if s1[i1] == s2[i2]:
                table[i1][i2] = table[i1 - 1][i2 - 1] + 1
            else:
                table[i1][i2] = max(table[i1 - 1][i2], table[i1][i2 - 1])
    # print(table)
    return table[l1][l2]


if __name__ == '__main__':
    # s1, s2 = input(), input()
    # s1, s2 = 'SHINCHAN', 'NOHARAAA'
    # s1, s2 = 'ABCDEF', 'FBDAMN'
    # s1, s2 = 'HARRY', 'SALLY'
    # s1, s2 = 'AA', 'BB'
    # s1, s2 = 'ELGGYJWKTDHLXJRBJLRYEJWVSUFZKYHOIKBGTVUTTOCGMLEXWDSXEBKRZTQUVCJNGKKRMUUBACVOEQKBFFYBUQEMYNENKYYGUZSP', 'FRVIFOVJYQLVZMFBNRUTIYFBMFFFRZVBYINXLDDSVMPWSQGJZYTKMZIPEGMVOUQBKYEWEYVOLSHCMHPAZYTENRNONTJWDANAMFRX'

    print(commonChild(s1, s2))
