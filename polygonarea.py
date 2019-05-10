class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return 'Point(%s , %s)' % (self.x, self.y)


def ccw(a, b, c):
    ab, ac = Point(b.x - a.x, b.y - a.y), Point(c.x - a.x, c.y - a.y)
    return ab.x * ac.y - ab.y * ac.x


def polygon_area(points):
    area, n = 0, len(points)

    def r(v): return (v + 1) % n

    for i in range(0, n):
        area += points[r(i)].x * \
                (points[r(i + 1)].y - points[r(i - 1)].y)
    return (area / 2.0)


n = int(input())
while n > 0:
    points = []
    for i in range(n):
        x, y = map(float, input().split())
        points.append(Point(x, y))
    area = polygon_area(points)
    D = 'CCW' if area > 0 else 'CW'
    print('%s %.1f' % (D, abs(area)))
    n = int(input())
