"""Example of building subplots"""

import pyplots
import numpy as np


def main():
    # Create sub plot of two rows and columns
    plot = pyplots.cartesian.SubPlots(2, 2)

    # x values for plotting
    x = np.linspace(-1, 1, 100)
    
    # upper left line
    line_ul = pyplots.cartesian.Line(x, x ** 0)

    # upper right line
    line_ur = pyplots.cartesian.Line(x, x ** 1)

    # lower left line
    line_ll = pyplots.cartesian.Line(x, x ** 3)

    # Lower right line
    line_lr = pyplots.cartesian.Line(x, x ** 4)

    # Add lines
    plot[0, 0].add(line_ul)
    plot[0, 1].add(line_ur)
    plot[1, 0].add(line_ll)
    plot[1, 1].add(line_lr)

    # Show plot
    plot.show()



if __name__ == "__main__":
    main()
