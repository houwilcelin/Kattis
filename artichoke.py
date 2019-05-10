# -*- coding: utf-8 -*-
import math

p, a, b, c, d, n = map(int, input().split())
current_min = p * (math.sin(a * n + b) + math.cos(c * n + d) + 2)
o = 0
for i in range(n - 2, -1, -1):
    pri = p * (math.sin(a * (i + 1) + b) + math.cos(c * (i + 1) + d) + 2)
    if o < pri - current_min:
        o = pri - current_min
    if pri < current_min:
        current_min = pri
print("%.6f" % o)
