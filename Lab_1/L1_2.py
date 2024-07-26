# DFS
graph = {
    "A": ["B", "D", "F"],
    "B": ["C", "D"],
    "C": ["E", "A"],
    "D": ["C"],
    "E": ["F", "B"],
    "F": ["A"],
}

visited = []


def dfs(node):
    print(f"Visited - {node}")
    visited.append(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node)


dfs("A")
