def prims_algorithm(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True
    edges = []
    while sum(selected) < n:
        min_edge = [None, None, float('inf')]
        
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] < min_edge[2]:
                        min_edge = [i, j, graph[i][j]]
        edges.append(min_edge)
        selected[min_edge[1]] = True
    return edges
if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    result = prims_algorithm(graph)
    print("Edges in the Minimum Spanning Tree:")
    for edge in result:
        print(f"Edge: {chr(ord('A') + edge[0])} - {chr(ord('A') + edge[1])}, Weight: {edge[2]}")
