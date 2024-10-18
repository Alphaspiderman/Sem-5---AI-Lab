import random


graph = {
    "A": ["B", "D", "F"],
    "B": ["C", "D"],
    "C": ["E", "A"],
    "D": ["C"],
    "E": ["F", "B"],
    "F": ["A"],
}

h = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 0, "F": 4}


vc = {}
visited = set()
queue = []
src = "A"
dest = "E"

# Generate Costs
for key, val in graph.items():
    for entry in val:
        vc[(key, entry)] = random.randint(1, 10)


def best_fs(start, goal):
    queue.append((0, start, list(), 0))
    while queue:
        _, node, path, cost = queue.pop(0)
        if node == goal:
            print(f"Cost: {cost}")
            return path + [node]
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(
                    (
                        h[neighbour],
                        neighbour,
                        path + [node],
                        cost + vc[(node, neighbour)],
                    )
                )

        queue.sort()


for k, v in vc.items():
    print(f"Cost of {k}: {v}")
soln = best_fs(src, dest)
if soln:
    print(f"Path: {soln}")
else:
    print("No Path")
