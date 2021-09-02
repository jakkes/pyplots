import os

from matplotlib.legend import Legend
import plots
from plots import cartesian
import itertools
import numpy as np


def plot(i, x, y1, y2, logx, logy, legend, legend_location):
    plt = cartesian.Plot(logx=logx, logy=logy, legend=legend, legend_location=legend_location)
    plt.add_object(cartesian.Line(x, y1, label="Line one"))
    plt.add_object(cartesian.Line(x, y2, label="Line two"))
    plt.save(f"local/tests/cartesian/test_plots/logx-{logx}-logy-{logy}-legend_loc-{legend_location}.png")


def test_plots():
    x = np.linspace(-1, 1, 51)
    y1 = x ** 2
    y2 = x ** 3
    
    os.makedirs("local/tests/cartesian/test_plots", exist_ok=True)

    args = itertools.product(
        [x],
        [y1],
        [y2],
        [True, False],
        [True, False],
        [True],
        [plots.Legend.Location.BEST, plots.Legend.Location.CENTER]
    )
    for i, arg in enumerate(args):
        plot(i, *arg)
