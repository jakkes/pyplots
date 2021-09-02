from typing import Dict, Optional, Tuple, Union
import uuid

import matplotlib.pyplot as plt

import plots
import plots.cartesian as cartesian


class Plot(plots.BasePlot):
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

        # Dictionary of object -> None, works like a ordered hash set.
        self._plot_objects: Dict[cartesian.PlotObject, None] = {}

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
