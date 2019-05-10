# -*- coding: utf-8 -*-
inp = input()
while inp != '0':
    perm = list(map(lambda n: int(n)-1, inp.split()[1:]))
    msg = input()
    msg_e = ''
    if len(perm) > 1:
        if len(msg) % len(perm) != 0:
            msg += ' '*(len(perm) - len(msg) % len(perm))
        for i in range(len(msg) // len(perm)):
            # print(i)
            for j in range(len(perm)):
                msg_e += msg[i*len(perm)+perm[j]]
            # print(msg_e)
    else:
        msg_e = msg
    print("'%s'" % msg_e)
    # print(list(msg))
    inp = input()
