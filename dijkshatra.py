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

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}

source_vertex = 'A'
minimum_spanning_tree = dijkstra_mst(graph, source_vertex)
print("Minimum Spanning Tree (Dijkstra's Algorithm):", minimum_spanning_tree)