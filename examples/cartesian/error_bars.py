"""Example of working with error bars."""

import numpy as np
from pyplots import cartesian


def main():
    
    # Create plot
    plot = cartesian.Plot(legend=True)

    # Create x and y values
    x = np.linspace(-1, 1, 10)
    y1 = x ** 2
    y2 = x ** 4

    # Create lines and add them to the plot
    line1 = cartesian.Line(x, y1, label="y=x^2")
    plot.add_object(line1)
    
    line2 = cartesian.Line(x, y2, label="y=x^4")
    plot.add_object(line2)
    
    # Assume x contains up to 5% error, for whatever reason, and that the error is
    # propagated to y.
    x_error = x * 0.05
    y1_error = y1 * 1.05**2
    y2_error = y2 * 1.05**4

    # Create error bars
    error1 = cartesian.Line.ErrorBars(x_error, y1_error)
    error2 = cartesian.Line.ErrorBars(x_error, y2_error)

    # Add error bars
    line1.error_bars(error1)
    line2.error_bars(error2)

    # Show plot
    plot.show()


if __name__ == "__main__":
    main()
