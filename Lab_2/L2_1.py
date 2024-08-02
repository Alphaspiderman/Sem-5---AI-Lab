# Uniform Cost Search
import random

graph = {
    "A": ["B", "D", "F"],
    "B": ["C", "D"],
    "C": ["E", "A"],
    "D": ["C"],
    "E": ["F", "B"],
    "F": ["A"],
}

vertice_cost = {}
visited = set()
queue = []
src = "A"
dest = "E"
queue.append((0, src, list()))

# Generate Costs
for key, val in graph.items():
    for entry in val:
        vertice_cost[(key, entry)] = random.randint(1, 15)

print(vertice_cost)

while queue:
    curr_cost, node, path = queue.pop(0)
    updated_path = path.copy()
    updated_path.append(node)
    if node == dest:
        print(f"Path: {updated_path}")
        print(f"Cost to Dest ({dest}) - {curr_cost}")
        quit()
    visited.add(node)
    for elem in graph[node]:
        cost = vertice_cost[(node, elem)] + curr_cost
        if elem not in visited:
            queue.append((cost, elem, updated_path))
    queue.sort()
    # print(queue)
