def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]


def unite(x, y):
    p[find(x)] = find(y)


n, m = tuple(map(int, (input().split(" "))))
p = list(range(n))
for i in range(m):
    a, b = tuple(map(lambda n: int(n) - 1, (input().split(" "))))
    unite(a, b)
c_0 = find(0)
connect = True
for i in range(1,n):
    if find(i) != c_0:
        print(i+1)
        connect = False
if connect:
    print("Connected")

