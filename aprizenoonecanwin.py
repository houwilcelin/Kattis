N, X = map(int, input().split(" "))
n_i = 0
max_i = 0
n_s = 0
min_s = 10 ** 9
art = list(map(int, input().split(" ")))
for val in art:
    if val <= X / 2:
        n_i += 1
        max_i = max(max_i, val)
    else:
        n_s += 1
        min_s = min(min_s, val)
if (n_i + n_s < 2) or (n_i == 0):
    print(1)
else:
    print(n_i + (1 if (min_s + max_i <= X) else 0))
