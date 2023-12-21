V = 4
INF = 99999

def floydWarshall(graph):
    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    printSolution(dist)

def printSolution(dist):
    print("Shortest distances between every pair of vertices:")
    for row in dist:
        print("\t".join(str(val) if val != INF else "INF" for val in row))

if __name__ == "__main__":
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    floydWarshall(graph)
