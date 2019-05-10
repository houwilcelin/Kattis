def bezout_coefs(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, u, v = bezout_coefs(b, a % b)
        return gcd, v, u - (a // b) * v


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


for _ in range(int(input())):
    a, n, b, m = map(int, input().split())
    gc, j, k = bezout_coefs(n, m)
    if (b - a) % gc == 0:
        # print(pgcd, j, k)
        x, K = a + j * n * (b - a) // gc, (m * n) // gc
        print(x % K, K)
    else:
        print('no solution')
