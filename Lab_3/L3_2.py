import random
import numpy as np

ls = np.random.randint(1, 99, (10, 10))
print(f"Matrix: \n", ls)


def find_neighbours(init_x, init_y):
    valid_states = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            x_val = init_x + i
            y_val = init_y + j
            # if x_val in range(0, ls.shape[0]) and y_val in range(0, ls.shape[1]):
            if 0 < x_val < ls.shape[0] and 0 < y_val < ls.shape[1]:
                valid_states.append((x_val, y_val))
    # print(f"State: ({x}, {y})")
    # print(f"Neighbours: {valid_states}")
    return valid_states


def hill_climb():
    x = random.randint(0, ls.shape[0] - 1)
    y = random.randint(0, ls.shape[1] - 1)
    # print(f"Init State Val: {ls[x][y]}")``
    print(f"Start State: ({x}, {y}) with Value: {ls[x][y]}")
    for i in range(50):
        neighbours = find_neighbours(x, y)
        # def f(x):
        #     print(x, ls[x[0]][x[1]])
        #     return ls[x[0]][x[1]]
        # s = max(neighbours, key=lambda s:f(s))
        # print(s)
        # print(ls[s[0]][s[1]])
        n_x, n_y = max(neighbours, key=lambda x: ls[x[0]][x[1]])
        # print(n_x, n_y)
        if ls[x][y] >= ls[n_x][n_y]:
            break
        x, y = n_x, n_y
        print(f"Travelling to: ({x}, {y}) with Value: {ls[x][y]}")
    return x, y


x, y = hill_climb()
print(f"Optimal State: ({x},{y}) with value {ls[x][y]}")
