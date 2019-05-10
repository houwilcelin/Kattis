def xor(inp):
    h = ord(inp[0])
    for i in range(1, len(inp)):
        h ^= ord(inp[i])
    return h


def comb(n):
    return (n*(n-1)) // 2


n = int(input())
while n != 0:
    hashs = {}
    ens = set()
    c = 0
    for i in range(n):
        line = input()
        h = xor(line)
        #old_len = len(ens)
        ens.add(line)
        hashs[h] = hashs.get(h, {})
        hashs[h][line] = hashs[h].get(line, 0) + 1
        hashs[h]['_s'] = hashs[h].get('_s', 0) + 1 # Total sum
    for k in hashs.keys():
        c+= comb(hashs[k]['_s']) #
        for lk in hashs[k].keys():
            if lk != '_s':
                c-= comb(hashs[k][lk])
    print(len(ens), c)
    n = int(input())