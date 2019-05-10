# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


def next_(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3*x + 1


"""n_m = 0
x_m = 10**6
for i in range(5, 10**6+1):
    n = 0
    x = i
    while x != 1 and n < 1000:
        if x % 2 == 0:
            x /= 2
            # print('p->', x)
        else:
            x = 3*x + 1
            # print('i->', x)
        n += 1
        if x > x_m:
            print(i, n, x)
            x_m = x
        #x_m = max(x_m,x)
    #
    n_m = max(n_m, n)
"""
a, b = map(int, input().split())
while (a, b) != (0, 0):
    if a == b:
        print("%d needs %d steps, %d needs %d steps, they meet at %d" %
              (a, 0, b, 0, a))
    else:
        tab = {}#[None] * (3*10**6+1)
        tab[a] = 0, 0
        tab[b] = 1, 0
        a_, b_ = a, b
        for i in range(1, 525):
            if a != 1:
                a = next_(a)
                if tab.get(a) == None:
                    tab[a] = 0, i
                #print('a,%d->%d' % (i, a))
            if b != 1:
                b = next_(b)
                #print('b,%d->%d' % (i, b))
                if tab.get(b) == None:
                    tab[b] = 1, i
            if tab.get(a) != None and tab[a][0] != 0:
                print("%d needs %d steps, %d needs %d steps, they meet at %d" %
                      (a_, i, b_, tab[a][1], a))
                break
            if tab.get(b) != None and tab[b][0] != 1:
                print("%d needs %d steps, %d needs %d steps, they meet at %d" %
                      (a_, tab[b][1], b_, i, b))
                break
    a, b = map(int, input().split())
