import heapq

def dijkstra(graph, start):
    priority_queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example graph
example_graph = {
    'A': {'B': 3, 'C': 5},
    'B': {'A': 4, 'C': 2, 'D': 7},
    'C': {'A': 8, 'B': 2, 'D': 1},
    'D': {'B': 6, 'C': 1}
}

# Starting vertex
start_vertex = 'A'

# Run Dijkstra's algorithm
result = dijkstra(example_graph, start_vertex)

# Print the result
print("\nShortest distances from the start vertex:")
for vertex, distance in result.items():
    print(f"To {vertex}: {distance}")
