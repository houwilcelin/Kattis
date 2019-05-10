# -*- coding: utf-8 -*-
#import networkx as nx

class Node:
    def __init__(self, _id, parent=None):
        self.id = _id
        self.adjacents = []
        self.parent = parent

    def adj(self, o):
        self.adjacents.append(o)

    def set_parent(self, o):
        node = self.copy()
        node.parent = o
        node.adjacents.remove(o)
        return node

    def copy(self):
        node = Node(self.id)
        node.adjacents = self.adjacents[:]
        return node


class Graph:
    def __init__(self, n, m):
        #self.edges =  [(0, 1), (0, 2), (0, 5), (0, 6), (1, 3), (2, 4), (1, 2), (1, 2),(1, 5), (2, 6), (5, 6)]
        self.edges = []
        self.added = {}
        self.deg = [0 for _ in range(n)]
        self.n, self.m = n, m
        self.nodes = [Node(i) for i in range(n)]

    def add_edge(self, i, j):
        self.deg[i] += 1
        if self.added.get((i, j), None) == None and self.added.get((j, i), None) == None:
            self.nodes[i].adj(j)
            self.nodes[j].adj(i)
            self.edges.append((i, j))
            self.added[(i, j)] = True

    def draw(self):
        G = nx.Graph()
        G.add_nodes_from(range(self.n))
        G.add_edges_from(self.edges)
        nx.draw_networkx(G, with_labels=True)

    def make_acyclic(self):
        #self.edges = list(set(self.edges))
        visited = [False for _ in range(self.n)]
        fringe = [self.nodes[0]]
        while len(fringe) > 0:
            node = fringe.pop()
            #print('visite %d' % node.id)
            if not visited[node.id]:
                visited[node.id] = True
                fringe.extend([self.nodes[adj].set_parent(node.id)
                               for adj in node.adjacents])
            else:
                try:
                    self.edges.remove((node.parent, node.id))
                    #print('Remove (%d,%d)' % (node.parent, node.id))
                except:
                    pass
                    #print('Cannot (%d,%d)' % (node.parent, node.id))


n, m = map(int, input().split())
graph = Graph(n, m)
for _ in range(m):
    i, j = map(int, input().split())
    graph.add_edge(i, j)

#print(graph.edges)"""
"""ed = [(0, 1), (0, 2), (0, 5), (0, 6), (1, 3), (2, 4), (1, 2), (1, 2),
      (1, 5), (2, 6), (5, 6)]
graph = Graph(7, 11)
for i, j in ed:
    graph.add_edge(i, j)"""
# graph.draw()
graph.make_acyclic()
#graph.draw()
print(graph.n, len(graph.edges))
print("\n".join(map(lambda n: "%d %d"%n,graph.edges)))

"""
4 3
0 1
2 1
2 3
"""
"""
7 11
0 1
0 2
0 5
0 6
1 3
2 4
1 2
1 2
1 5
2 6
5 6
"""
