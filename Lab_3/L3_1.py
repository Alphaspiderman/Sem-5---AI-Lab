from math import cos, sin
import random
from typing import Callable, List

space = [i for i in range(-20, 20)]


def f(x):
    return x * sin(x) - cos(x)


def hill_climb(f: Callable, space: List, max_iter: int = 1000):
    sol = random.choice(space)
    print(f"Inital Solution: {sol}")
    for i in range(max_iter):
        neighbours = [sol + dx for dx in (-1, -0.5, 0, 0.5, 1)]
        next_val = max(neighbours, key=lambda x: f(x))
        if f(next_val) <= f(sol):
            break

        sol = next_val
    return sol


max_val = hill_climb(f, space)

print(f"Maximum State: {max_val}")
print(f"Value of State: {round(f(max_val), 2)}")
