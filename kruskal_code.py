class KruskalAlgorithm:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])
    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            rank[root_y] += 1
    def kruskal(self):
        result = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.vertices)]
        rank = [0] * self.vertices
        i = 0
        while len(result) < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            if x != y:
                result.append((u, v, w))
                self.union(parent, rank, x, y)
        return result
if __name__ == "__main__":
    kruskal_algo = KruskalAlgorithm(4)
    kruskal_algo.add_edge(0, 1, 10)
    kruskal_algo.add_edge(0, 2, 6)
    kruskal_algo.add_edge(0, 3, 5)
    kruskal_algo.add_edge(1, 3, 15)
    kruskal_algo.add_edge(2, 3, 4)
    result = kruskal_algo.kruskal()
    print("Edges in the Minimum Spanning Tree:")
    for edge in result:
        print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
