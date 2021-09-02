import os
import plots
from plots import cartesian
import itertools
import numpy as np


def plot(i, x, y1, y2, legend, legend_location):
    plt = cartesian.Plot(legend=legend, legend_location=legend_location)
    plt.add_object(cartesian.Line(x, y1, label="Line one"))
    plt.add_object(cartesian.Line(x, y2, label="Line two"))
    plt.save(f"local/tests/cartesian/test_plots/test_save{i}.png")


def test_plots():
    x = np.linspace(-1, 1, 51)
    y1 = x ** 2
    y2 = x ** 3
    
    os.makedirs("local/tests/cartesian/test_plots", exist_ok=True)

    args = itertools.product(
        [x],
        [y1],
        [y2],
        [True],
        plots.Legend.Location
    )
    for i, arg in enumerate(args):
        plot(i, *arg)
