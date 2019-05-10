# -*- coding: utf-8 -*-
import math
n, o = int(input()), 0
while n != 1:
    for i in range(2, int(math.sqrt(n))+2):
        if (n % i) == 0:
            n //= i
            o += 1
            break
        elif i == int(math.sqrt(n)) + 1:
            n = 1
            o += 1
            break
print(o)
#0.03s