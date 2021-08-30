"""Plots functions y=x, y=x^2, ..., y=x^5, for x in (-1, 1)."""

import numpy as np
from plots import cartesian


def main():

    # Select x values.
    x = np.linspace(-1, 1, 100)
    
    # Create a plot with cartesian axes. Let the plot include a legend.
    plot = cartesian.Plot(legend=True)

    for power in range(1, 6):
        
        # Compute y values.
        y = x ** power

        # Create a line of the x and y values.
        line = cartesian.Line(x, y, label=f"$y=x**{power}$")

        # Add line to the plot.
        plot.add_object(line)

    # Display plot.
    plot.show()


if __name__ == "__main__":
    main()
