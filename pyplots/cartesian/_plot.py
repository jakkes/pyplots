from typing import Dict, Optional, Tuple, Union
import uuid

import matplotlib.pyplot as plt

import pyplots
import pyplots.cartesian as cartesian


class Plot(pyplots.BasePlot):
    """Figure with a single plot of cartesian axes."""

    def __init__(
        self,
        size: Tuple[int, int] = (6.4, 4.8),
        logy: bool = False,
        logx: bool = False,
        xlabel: str = "",
        ylabel: str = "",
        title: str = "",
        legend: bool = False,
        legend_location: Union[
            "pyplots.Legend.Location", Tuple[int, int]
        ] = pyplots.Legend.Location.BEST,
        _owns_figure: bool = True,
    ):
        """
        Args:
            size (Tuple[int, int], optional): Size of the figure in inches,
                `(width, height)`. Defaults to (6.4, 4.8).
            logy (bool, optional): If True, the y-axis is logarithmic. Defaults to
                False.
            logx (bool, optional): If True, the x-axis is logarithmic. Defaults to
                False.
            xlabel (str, optional): Label attached to the x-axis. Defaults to no label.
            ylabel (str, optional): Label attached to the y-axis. Defaults to no label.
            title (str, optional): Title of the plot. Defaults to no title.
            legend (bool, optional): If True, a legend is displayed. Defaults to False.
            legend_location (Union[Plot.Legend.Location, Tuple[int, int]], optional):
                Determines the location of the legend. Defaults to
                `Plot.Legend.Location.BEST`. May also be given in coordinates.
        """
        super().__init__(
            size=size,
            legend=legend,
            legend_location=legend_location,
            _owns_figure=_owns_figure,
        )

        self._logx = logx
        self._logy = logy
        self._title = title
        self._xlabel = xlabel
        self._ylabel = ylabel

        # Dictionary of object -> None, works like a ordered hash set.
        self._plot_objects: Dict[cartesian.PlotObject, None] = {}

    @property
    def logx(self) -> bool:
        """If True, the x-axis is rendered in logarithmic scale."""
        return self._logx

    @logx.setter
    def logx(self, val: bool):
        self._logx = val

    @property
    def logy(self) -> bool:
        """If True, the y-axis is rendered in logarithmic scale."""
        return self._logy

    @logy.setter
    def logy(self, val: bool):
        self._logy = val

    @property
    def xlabel(self) -> str:
        """Label attached to the x-axis."""
        return self._xlabel

    @xlabel.setter
    def xlabel(self, val: str):
        self._xlabel = val

    @property
    def ylabel(self) -> str:
        """Label attached to the y-axis."""
        return self._ylabel

    @ylabel.setter
    def ylabel(self, val: str):
        self._ylabel = val

    @property
    def title(self) -> str:
        """Title of the plot."""
        return self._title

    @title.setter
    def title(self, val: str):
        self._title = val

    def add_object(self, obj: cartesian.PlotObject):
        self._plot_objects[obj] = None

    def remove_object(self, obj: cartesian.PlotObject):
        del self._plot_objects[obj]

    def _generate_axes(self) -> plt.Axes:
        return plt.axes()

    def _render(self, axes: plt.Axes):
        for obj in self._plot_objects:
            obj._render(axes)

    def _post_render(self, axes: plt.Axes):
        super()._post_render(axes)
        
        if self._logx:
            axes.set_xscale("log")
        if self._logy:
            axes.set_yscale("log")

        axes.set_xlabel(self._xlabel)
        axes.set_ylabel(self._ylabel)
        axes.set_title(self._title)
