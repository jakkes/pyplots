"""Example of working with error bars."""

import numpy as np
from plots import cartesian


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
    
    # Assume x contains up to 5% error, for whatever reason
    x_error = cartesian.Line.ErrorBars.symmetric(x * 0.05)
    line1.set_x_error_bars(x_error)
    line2.set_x_error_bars(x_error)

    # Let this error propagate through x^2 and x^4
    y1_error = cartesian.Line.ErrorBars.symmetric(y1 * 1.05**2)
    line1.set_y_error_bars(y1_error)

    y2_error = cartesian.Line.ErrorBars.symmetric(y2 * 1.05**4)
    line2.set_y_error_bars(y2_error)

    # Show plot
    plot.show()


if __name__ == "__main__":
    main()
