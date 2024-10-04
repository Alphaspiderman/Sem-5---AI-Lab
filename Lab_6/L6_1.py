def solve(max_j1, max_j2, goal):
    q = [[(0, 0), ["Initally Empty"]]]
    visited = set()
    visited.add((0, 0))
    while q:
        (j1, j2), p = q.pop(0)
        if j1 == goal or j2 == goal:
            return path

        states = [
            ((max_j1, j2), p + ["Fill Jug 1"]),
            ((j1, max_j2), p + ["Fill Jug 2"]),
            ((0, j2), p + ["Empty Jug 1"]),
            ((j1, 0), p + ["Empty Jug 2"]),
            (
                (min(max_j1, j1 + j2), j2 - ((min(max_j1, j1 + j2) - j1))),
                p + ["Transfer from 2 to 1"],
            ),
            (
                (j1 - ((min(max_j2, j1 + j2) - j2)), min(max_j2, j1 + j2)),
                p + ["Transfer from 1 to 2"],
            ),
        ]

        for (nj1, nj2), path in states:
            if (nj1, nj2) not in visited:
                if nj1 > max_j1 or nj2 > max_j2:
                    pass
                else:
                    q.append(((nj1, nj2), path))


jug_1 = int(input("Capacity of Jug 1: "))
jug_2 = int(input("Capacity of Jug 2: "))
required = int(input("Required Capacity: "))

path = solve(jug_1, jug_2, required)
if path:
    print(f"States followed - {path}")
else:
    print("No Solution")
