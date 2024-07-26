# BFS
graph = {
    "A": ["B", "D", "F"],
    "B": ["C", "D"],
    "C": ["E", "A"],
    "D": ["C"],
    "E": ["F", "B"],
    "F": ["A"],
}
queue = []
visited = []


def bfs():
    while queue:
        elem = queue.pop(0)
        visited.append(elem)
        print(f"Visited - {elem}")

        for neighbour in graph[elem]:
            if neighbour not in visited + queue:
                queue.append(neighbour)


queue.append("C")
bfs()
