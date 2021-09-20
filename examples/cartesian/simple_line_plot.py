"""Plots functions y=x and y=x^2 for x in (-1, 1)."""

import numpy as np
from pyplots import cartesian


def main():

    # Select x values.
    x = np.linspace(-1, 1, 100)
    
    # Create a plot with cartesian axes. Let the plot include a legend.
    plot = cartesian.Plot(legend=True)

    # Create a line of y=x
    line = cartesian.Line(x, x, label="y=x")

    # Add line to plot
    plot.add(line)

    # Create a line of y=x^2
    line = cartesian.Line(x, x**2, label="y=x^2")

    # Add line to plot
    plot.add(line)

    # Display plot.
    plot.show()


if __name__ == "__main__":
    main()
