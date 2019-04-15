#!/usr/bin/evn python
# -*- coding: utf-8 -*-
while True:
    try:
        n, k = map(int, input().strip().split())
        LT = []
        for _ in range(n):
            LT.append(tuple(map(int, input().strip().split())))
        LT.sort(key=lambda lt: lt[0], reverse=True)

        r, i = 0, 0
        for lt in LT:
            if not lt[1]:
                r += lt[0]
            elif i < k:
                r += lt[0]
                i += 1
            else:
                r -= lt[0]

        print(r)
    except:
        break
