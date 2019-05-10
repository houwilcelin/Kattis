def maxcolinear(pts):
    maxPoint = 0
    n = len(pts)
    slopes = {}
    for i in range(n):
        for j in range(i + 1, n):
            if (pts[j]['x'] - pts[i]['x']) != 0:
                f = ((pts[j]['y'] - pts[i]['y']) / (pts[j]['x'] - pts[i]['x']))
                slopes[f] = slopes.get(f, 0) + 1
                maxPoint = max(maxPoint, slopes[f])
        slopes.clear()
    return maxPoint + 1


n = int(input())
while n > 0:
    print(maxcolinear([dict(zip(["x", "y"], map(int, input().split()))) for _ in range(n)]))
    n = int(input())
