# -*- coding: utf-8 -*-
import math
while True:
    try:
        txt = input()
        counter = dict(
            zip([chr(i) for i in (list(range(97, 123))+list(range(65, 91)))], [0]*52))
        base = 1
        for l in txt:
            counter[l] += 1
            base *= counter[l]
        print(math.factorial(len(txt)) // base)
    except:
        exit(0)
