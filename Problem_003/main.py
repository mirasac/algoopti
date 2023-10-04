import matplotlib.pyplot as plt
import numpy as np

MAX_DEPTH = 10

# Naive solution, computation time O(3^n).
def f(x, y, lx, ly, ax):
    print(f"(x, y, lx, ly) = ({x}, {y}, {lx}, {ly})")
    ax.plot([x, x + lx, x, x], [y, y, y + ly, y])
    lx = lx / 2
    ly = ly / 2
    if lx >= MAX_DEPTH and ly >= MAX_DEPTH:
        f(x, y, lx, ly, ax)
        f(x + lx, y, lx, ly, ax)
        f(x, y + ly, lx, ly, ax)

def main():
    fig, ax = plt.subplots()
    f(0, 0, 1000, 1000, ax)
    plt.show()

main()
