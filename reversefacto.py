# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:43:47 2019

@author: Jocelin
"""

import math
import time
simple_facto = dict(zip([1, 2, 6, 24, 120, 720], range(1, 8)))
# '1'= 1,'2'=2,'6'=3,'24'=4,'120'=5,'720'=6)

"""for i,val in enumerate([1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]):
    simple_facto[val] = i"""
n = input()
k = len(n)
start = time.time()
if k < 4:
    print(simple_facto[int(n)])
else:
    ln, i = 2.857332496431268, 7  # 5.559763032876794,10
    while True:
        ln += math.log10(i)
        if (int(ln)+1) == k:
            print('Found : %d in %s' % (i, time.time()-start))
            # print(i)
            break
        else:
            print('%d:%s' % (i, ln))
        i += 1
    # print('Nothing')
