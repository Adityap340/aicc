import heapq

def dijkstra_mst(graph, source):
    mst = []
    visited = set()
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    pq = [(0, source, None)]  # (distance, vertex, parent)
    while pq:
        dist, current_vertex, parent = heapq.heappop(pq)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        if parent is not None:
            mst.append((parent, current_vertex, dist))
        for neighbor, weight in graph[current_vertex].items():
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor, current_vertex))
                distances[neighbor] = min(distances[neighbor], weight)
    return mst

# Get input from the user
num_vertices = int(input("Enter the number of vertices: "))
graph = {}
print("Enter the edges (source, destination, weight):")
for _ in range(num_vertices):
    source, dest, weight = input().split()
    if source not in graph:
        graph[source] = {}
    graph[source][dest] = int(weight)

source_vertex = input("Enter the source vertex: ")

# Compute the minimum spanning tree
minimum_spanning_tree = dijkstra_mst(graph, source_vertex)
print("Minimum Spanning Tree (Dijkstra's Algorithm):", minimum_spanning_tree)


# Enter the number of vertices: 4
# Enter the edges (source, destination, weight):
# A B 4
# A C 2
# B C 5
# B D 10
# C D 3
# Enter the source vertex: A