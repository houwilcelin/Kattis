def bezout_coefs(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, u, v = bezout_coefs(b, a % b)
        return gcd, v, u - (a // b) * v


n, t = map(int, input().split())
while (n, t) != (0, 0):
    for i in range(t):
        a, op, b = input().split()
        # print(a, op, b)
        a, b = int(a), int(b)
        if op == '*':
            print((a * b) % n)
        elif op == '+':
            print((a + b) % n)
        elif op == '-':
            print((a - b) % n)
        elif op == '/':
            if b == 0:
                print(-1)
            else:
                gcd, u, v = bezout_coefs(b, n)
                if gcd != 1:
                    print(-1)
                else:
                    print((a * (u % n)) % n)
    n, t = map(int, input().split())
