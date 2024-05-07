class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1


def kruskal_mst(graph):
    disjoint_set = DisjointSet()
    mst = []
    edges = sorted((weight, u, v) for u in graph for v, weight in graph[u].items())

    for vertex in graph:
        disjoint_set.make_set(vertex)

    for weight, u, v in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))

    return mst


def take_input():
    graph = {}
    for _ in range(int(input("Enter the number of edges: "))):
        u, v, w = input("Enter edge (source destination weight): ").split()
        w = int(w)
        graph.setdefault(u, {})[v] = w
        graph.setdefault(v, {})[u] = w
    return graph


graph = take_input()
mst = kruskal_mst(graph)
print("Minimum Spanning Tree (Kruskal's Algorithm):", mst)


# Enter the number of edges:  10
# Enter edge (source destination weight):  a b 6
# Enter edge (source destination weight):  a g 15
# Enter edge (source destination weight):  b c 11
# Enter edge (source destination weight):  g c 25
# Enter edge (source destination weight):  b d 5
# Enter edge (source destination weight):  g f 12
# Enter edge (source destination weight):  c d 17
# Enter edge (source destination weight):  c f 9
# Enter edge (source destination weight):  d e 22
# Enter edge (source destination weight):  f e 10
# Minimum Spanning Tree (Kruskal's Algorithm): [('b', 'd', 5), ('a', 'b', 6), ('c', 'f', 9), ('e', 'f', 10), ('b', 'c', 11), ('f', 'g', 12)]