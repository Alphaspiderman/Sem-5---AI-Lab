def valid(left, right):
    lm, lc = left
    rm, rc = right
    # Ensure we do not have -ve number of people
    if lm >= 0 and lc >= 0 and rm >= 0 and rc >= 0:
        # Ensure we follow rules of the game
        if lm == 0:
            return rm >= rc
        if rm == 0:
            return lm >= lc
        return lm >= lc and rm >= rc
    return False


def solve(inm, inc):
    q = [((inm, inc), (0, 0), "L")]
    b = {((inm, inc), (0, 0), "L"): None}
    while q:
        left, right, boat = q.pop(0)
        if left == (0, 0) and right == (inm, inc):
            state = (left, right, boat)
            path = [state]
            while b[state] != None:
                path.append(state)
                state = b[state]
            return path
        lm, lc = left
        rm, rc = right
        children = []
        for i in range(3):  # M to Move
            for j in range(3):  # C to Move
                if i + j in (1, 2):
                    if boat == "L":  # L -> R
                        child = ((lm - i, lc - j), (rm + i, rc + j), "R")
                    if boat == "R":  # L <- R
                        child = ((lm + i, lc + j), (rm - i, rc - j), "L")
                    children.append(child)
        for c in children:
            if c not in b.keys() and valid(c[0], c[1]):
                b[c] = (left, right, boat)
                q.append(c)


path = solve(3, 3)
if path:
    print(f"States followed - ")
    for loc in path[::-1]:
        print(loc)
else:
    print("No Solution")
