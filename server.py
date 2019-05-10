n, T = tuple(map(int, input().split()))
time = 0
nbr = 0
for i in list(map(int, input().split())):
    time += i
    if time > T:
        break
    else:
        nbr += 1
print(nbr)
