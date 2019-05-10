import itertools
for _ in range(int(input())):
    input()
    N = int(input())
    t = list(map(int,input().split()))
    t_sum = list(itertools.accumulate(t))
    data, c = {}, 0
    for i in range(N-1,-1,-1):
        a = t_sum[i]
        c+= data.get(a+47,0)
        data[a] = data.get(a,0) + 1
    print(c + data.get(47,0))