from enum import Enum
from typing import Set, Tuple, Union
import uuid

import matplotlib.pyplot as plt

import plots.cartesian as cartesian


def _get_plot_fn(logx: bool, logy: bool):
    if logy and logx:
        return plt.loglog
    elif logy:
        return plt.semilogy
    elif logx:
        return plt.semilogx
    else:
        return plt.plot


class LegendLocation(str, Enum):
    BEST = "best"
    UPPER_LEFT = "upper left"
    UPPER_CENTER = "upper center"
    UPPER_RIGHT = "upper right"
    CENTER_LEFT = "center left"
    CENTER = "center"
    CENTER_RIGHT = "center right"
    LOWER_LEFT = "lower left"
    LOWER_CENTER = "lower center"
    LOWER_RIGHT = "lower right"


class Plot:
    """Figure with a single plot of cartesian axes."""

    class Legend:
        Location = LegendLocation

    def __init__(
        self,
        size: Tuple[int, int] = (6.4, 4.8),
        logy: bool = False,
        logx: bool = False,
        legend: bool = False,
        legend_location: Union[
            "Plot.Legend.Location", Tuple[int, int]
        ] = LegendLocation.BEST,
    ):
        """
        Args:
            size (Tuple[int, int], optional): Size of the figure in inches,
                `(width, height)`. Defaults to (6.4, 4.8).
            logy (bool, optional): If True, the y-axis is logarithmic. Defaults to
                False.
            logx (bool, optional): If True, the x-axis is logarithmic. Defaults to
                False.
            legend (bool, optional): If True, a legend is displayed. Defaults to False.
            legend_location (Union[Plot.Legend.Location, Tuple[int, int]], optional):
                Determines the location of the legend. Defaults to
                `Plot.Legend.Location.BEST`. May also be given in coordinates.
        """
        self._id = str(uuid.uuid4())
        self._size = size
        self._plot_fn = _get_plot_fn(logx, logy)
        self._legend = legend
        self._legend_location = legend_location

        self._plot_objects: Set[cartesian.PlotObject] = set()

    def add_object(self, obj: cartesian.PlotObject):
        self._plot_objects.add(obj)

    def remove_object(self, obj: cartesian.PlotObject):
        self._plot_objects.remove(obj)

    def save(self, path: str):
        """Saves the plot to the given path.

        Args:
            path (str): File path to which the figure should be saved.
        """
        self._render()
        plt.savefig(path)
        self._close()

    def show(self):
        """Renders and displays the plot."""
        self._render()
        plt.show()
        self._close()

    def _close(self):
        """Closes the figure."""
        plt.close(self._id)

    def _render(self):
        plt.figure(self._id, self._size)
        for obj in self._plot_objects:
            obj._render(self._plot_fn)

        if self._legend:
            plt.legend(loc=self._legend_location)
