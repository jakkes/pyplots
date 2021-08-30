"""Example of building sub plots"""

import plots
import numpy as np


def main():
    plot = plots.cartesian.SubPlots(2, 2)
    x = np.linspace(-1, 1, 100)
    
    for row in range(2):
        for col in range(2):
            power = 2 * row + col
            y = x ** power
            line = plots.cartesian.Line(x, y)
            plot[row, col].add_object(line)

    plot.show()



if __name__ == "__main__":
    main()
