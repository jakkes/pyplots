import numpy as np
from pyplots import cartesian


def main():
    plot = cartesian.Plot()
    values = np.linspace(0, 1, 1024).reshape((-1, 1024)).repeat(1024, 0)
    plot.add(
        cartesian.Grid(values)
    )
    plot.show()


if __name__ == "__main__":
    main()
