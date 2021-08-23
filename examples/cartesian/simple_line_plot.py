"""Plots functions y=x, y=x^2, ..., y=x^5, for x in (-1, 1)."""

import numpy as np
from plots import cartesian


def main():
    x = np.linspace(-1, 1, 100)
    plot = cartesian.Plot()

    for power in range(1, 6):
        y = x ** power
        line = cartesian.Line(x, y)
        plot.add_object(line)

    plot.show()


if __name__ == "__main__":
    main()
