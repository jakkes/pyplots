from typing import Dict, Optional, Tuple, Union
import uuid

import matplotlib.pyplot as plt

import plots
import plots.cartesian as cartesian


def _get_plot_fn(ax: plt.Axes, logx: bool, logy: bool):
    if logy and logx:
        return ax.loglog
    elif logy:
        return ax.semilogy
    elif logx:
        return ax.semilogx
    else:
        return ax.plot


class Plot:
    """Figure with a single plot of cartesian axes."""

    def __init__(
        self,
        size: Tuple[int, int] = (6.4, 4.8),
        logy: bool = False,
        logx: bool = False,
        legend: bool = False,
        legend_location: Union[
            "plots.Legend.Location", Tuple[int, int]
        ] = plots.Legend.Location.BEST,
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
        self._id: Optional[str] = None
        self._size = size
        self._logx = logx
        self._logy = logy
        self._ax: plt.Axes = None
        self._legend = legend
        self._legend_location = legend_location

        # Dictionary of object -> None, works like a ordered hash set.
        self._plot_objects: Dict[cartesian.PlotObject, None] = {}

    def add_object(self, obj: cartesian.PlotObject):
        self._plot_objects[obj] = None

    def remove_object(self, obj: cartesian.PlotObject):
        del self._plot_objects[obj]

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
        if self._id is not None:
            plt.close(self._id)

    def _render(self):
        if self._ax is None:
            self._id = str(uuid.uuid4())
            plt.figure(self._id, self._size)
            self._ax = plt.axes()

        plot_fn = _get_plot_fn(self._ax, self._logx, self._logy)
        for obj in self._plot_objects:
            obj._render(plot_fn)

        if self._legend:
            plt.legend(loc=self._legend_location)

    def _set_ax(self, ax: plt.Axes):
        self._ax = ax
