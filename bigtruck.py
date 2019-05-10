import bisect


class Node:
    def __init__(self, _id, truck, c):
        self.id, self.truck = _id, truck
        self.c = c

    def __lt__(self, node):
        if self.c == node.c:
            return self.truck > node.truck
        return self.c < node.c

    def __repr__(self):
        return 'Node : %d, %d' % (self.id, self.truck)


def succesor(node):
    truck, c, s = node.truck, node.c, []
    for (b, d) in paths.get(node.id, []):
        s.append(Node(b, truck+trucks[b], c+d))
    return s


n = int(input())
trucks = list(map(int, input().replace('\n', '').split(' ')))
paths = {}
for _ in range(int(input())):
    a, b, d = map(int, input().replace('\n', '').split(' '))
    a, b = a-1, b-1
    paths[a], paths[b] = paths.get(a, []), paths.get(b, [])
    paths[a].append((b, d))
    paths[b].append((a, d))
closed = [False for _ in range(n)]
fringe = [Node(0, trucks[0], 0)]
while len(fringe) > 0:
    node = fringe.pop(0)
    if node.id != n-1 and not closed[node.id]:
        for no in succesor(node):
            bisect.insort(fringe, no)
        closed[node.id] = True
    elif node.id == n-1:
        print(node.c,node.truck)
        exit(0)
print('impossible')
