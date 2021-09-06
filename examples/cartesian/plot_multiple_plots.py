"""Plots functions y=x and y=x^2 for x in (-1, 1) in two separate windows."""

import numpy as np

import pyplots
from pyplots import cartesian


def main():

    # Select x values.
    x = np.linspace(-1, 1, 100)
    
    # Create a plot with cartesian axes. Let the plot include a legend.
    plot = cartesian.Plot(legend=True)

    # Create a line of y=x
    line = cartesian.Line(x, x, label="y=x")

    # Add line to plot
    plot.add_object(line)

    # Create a new plot
    plot2 = cartesian.Plot(legend=True)

    # Create a line of y=x^2
    line2 = cartesian.Line(x, x**2, label="y=x^2")

    # Add line to plot
    plot2.add_object(line2)

    # Display plots.
    pyplots.show(plot, plot2)


if __name__ == "__main__":
    main()
