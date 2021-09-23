"""Example of building subplots"""

import pyplots
import numpy as np


def main():
    # Create sub plot of two rows and columns
    plot = pyplots.cartesian.SubPlots(2, 2, sharex=True, sharey=True)

    # upper left line
    x_ul = np.linspace(-1, 0)
    line_ul = pyplots.cartesian.Line(x_ul, x_ul ** 0)

    # upper right line
    x_ur = np.linspace(0, 1)
    line_ur = pyplots.cartesian.Line(x_ur, x_ur ** 1)

    # lower left line
    x_ll = np.linspace(-2, 0)
    line_ll = pyplots.cartesian.Line(x_ll, x_ll ** 3)

    # Lower right line
    x_lr = np.linspace(0, 2)
    line_lr = pyplots.cartesian.Line(x_lr, x_lr ** 4)

    # Add lines
    plot[0, 0].add(line_ul)
    plot[0, 1].add(line_ur)
    plot[1, 0].add(line_ll)
    plot[1, 1].add(line_lr)

    # Show plot
    plot.show()


if __name__ == "__main__":
    main()
