import sys, math
start = (0, 0)
pos = start
min_x, max_x, min_y, max_y = 0, 0, 0, 0
path = [pos]
data = {}
for act in sys.stdin.readlines():
    act = act.rstrip()
    x, y = pos
    if act == "down":
        y += 1
    elif act == "up":
        y -= 1
    elif act == "left":
        x -= 1
    else:
        x += 1
    pos = x, y
    path.append(pos)
    data[pos] = True
    min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)
rx, ry = max_x - min_x + 1, max_y - min_y + 1
print('#' * (rx + 2))
for y in range(min_y, max_y + 1):
    row = '#'
    for x in range(min_x, max_x + 1):
        if (x, y) == (0, 0):
            row += 'S'
        elif (x, y) == path[-1]:
            row += 'E'
        elif data.get((x, y), False):
            row += '*'
        else:
            row += ' '
    row += '#'
    print(row)
print('#' * (rx + 2))

# print(min_x, max_x, min_y, max_y)
# print(path)
"""path = list(map(lambda p: (p[0] + ab(min_x), p[1] + math.abs(min_y)), path))
# print(path)
rx, ry = max_x - min_x + 1, max_y - min_y + 1
tab = [[' '] * rx for _ in range(ry)]
start = path.pop(0)
end = path.pop()
tab[start[1]][start[0]] = 'S'
tab[end[1]][end[0]] = 'E'
for x, y in path:
    tab[y][x] = '*'
print('#' * (rx + 2))
for i in range(ry):
    print(''.join(['#'] + tab[i] + ['#']))
print('#' * (rx + 2))
# exit()"""
