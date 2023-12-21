def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            process_node(node)
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
def process_node(node):
    print(f"Processing node: {node}")
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B', 'H'],
        'F': ['C'],
        'G': ['C'],
        'H': ['E']
    }
    dfs(graph, 'A')
