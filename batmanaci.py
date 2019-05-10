import time


def solve(n, k):
    if db_fib[n] == 1:
        return n
    n_2 = db_fib[n - 2]
    n_1 = db_fib[n - 1]
    if k <= n_2:
        return solve(n - 2, k)
    else:
        return solve(n - 1, k - n_2)


n, k = map(int, (input().split(" ")))
db_fib = [None for _ in range(n + 2)]
db_fib[1] = db_fib[2] = 1

#start = time.time()
if n > 2:
    last_n = None
    for j in range(3, n + 1):
        db_fib[j] = db_fib[j - 2] + db_fib[j - 1]
        if db_fib[j] >= k:
            last_n = j
            break
    if (n % 2 == 0) != (last_n % 2 == 0):
        last_n += 1
    #print("Last N:",last_n)
    idx = solve(last_n, k)
else:
    idx = n
print((['N', 'A'])[idx - 1])
# print("time %s" % (time.time() - start))
