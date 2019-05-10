CLEAR, SET, OR, AND = 'CLEAR', 'SET', 'OR', 'AND'
n = int(input())
while n != 0:
    t = ['?'] * 32
    for _ in range(n):
        r = input().split()
        if r[0] == SET:
            t[int(r[1])] = 1
        elif r[0] == CLEAR:
            t[int(r[1])] = 0
        elif r[0] == OR:
            i, j = int(r[1]), int(r[2])
            if t[i] != '?' and t[j] != '?':
                t[i] |= t[j]
            elif t[i] == 1 or t[j] == 1:
                t[i] = 1
            else:
                t[i] = '?'
        elif r[0] == AND:
            i, j = int(r[1]), int(r[2])
            if t[i] != '?' and t[j] != '?':
                t[i] &= t[j]
            elif t[i] == 0 or t[j] == 0:
                t[i] = 0
            else:
                t[i] = '?'
    print("".join(map(str,reversed(t))))
    n = int(input())