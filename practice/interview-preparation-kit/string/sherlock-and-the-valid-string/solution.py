#!/usr/bin/env python

import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    charMap = {}
    for char in s:
        charMap.setdefault(char, 0)
        charMap[char] += 1

    print(charMap)

    freqMap = {}
    for char in charMap:
        freqMap.setdefault(charMap[char], 0)
        freqMap[charMap[char]] += 1

    print(freqMap)

    if len(freqMap) > 2:
        return 'NO'

    if len(freqMap) == 1:
        return 'YES'

    if 1 in freqMap:
        return 'YES' if freqMap[1] == 1 else 'NO'

    freqs = sorted(freqMap.keys())
    print(freqs)
    if freqs[1] - freqs[0] == 1 and freqMap[freqs[1]] == 1:
        return 'YES'

    return 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    # s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
    s = 'abcdefghhgfedecba'
    # s = 'aaaabbcc'

    result = isValid(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
