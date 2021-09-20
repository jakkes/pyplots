from typing import Dict, List, Optional, Sequence, Tuple, Union
from dataclasses import asdict

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

        self.logx: bool = logx
        """If `True`, the x-axis is rendered in logarithmic scale."""

        self.logy: bool = logy
        """If `True`, the y-axis is rendered in logarithmic scale."""
        
        self.xlabel: str = xlabel
        """Label attached to the x-axis."""

        self.xlabel_format: pyplots.text.Format = pyplots.text.Format()
        """Format of the x-axis label."""
        
        self.ylabel: str = ylabel
        """Label attached to the y-axis."""

        self.ylabel_format: pyplots.text.Format = pyplots.text.Format()
        """Format of the y-axis label."""
        
        self.title: str = title
        """Title of the plot."""

        self.title_format: pyplots.text.Format = pyplots.text.Format()
        """Format of the title text."""
        
        self.xticks: List[float] = None
        """Ticks shown on the x-axis. If `None`, ticks are generated automatically."""

        self.xticks_labels: List[str] = None
        """Labels of the shown ticks. Must have the same length as `xticks`."""

        self.xticks_format = pyplots.text.Format()
        """Format object of the xticks."""

        self.yticks: List[float] = None
        """Ticks shown on the y-ayis. If `None`, ticks are generated automatically."""

        self.yticks_labels: List[str] = None
        """Labels of the shown ticks. Must have the same length as `yticks`."""

        self.yticks_format: pyplots.text.Format = pyplots.text.Format()
        """Format object of the yticks."""

        # Dictionary of object -> None, works like a ordered hash set.
        self.__plot_objects: Dict[cartesian.PlotObject, None] = {}

    def add(self, obj: cartesian.PlotObject):
        self.__plot_objects[obj] = None

    def remove_object(self, obj: cartesian.PlotObject):
        del self.__plot_objects[obj]

    def _generate_axes(self) -> plt.Axes:
        return plt.axes()

    def _render(self, axes: plt.Axes):
        for obj in self.__plot_objects:
            obj._render(axes)

    def _post_render(self, axes: plt.Axes):
        super()._post_render(axes)
        
        if self.logx:
            axes.set_xscale("log")
        if self.logy:
            axes.set_yscale("log")

        axes.set_xlabel(self.xlabel)
        axes.set_ylabel(self.ylabel)
        axes.set_title(self.title)

        if self.xticks is not None:
            axes.set_xticks(self.xticks)
            if self.xticks_labels is not None:
                axes.set_xticklabels(self.xticks_labels, **asdict(self.xticks_format))

        if self.yticks is not None:
            axes.set_yticks(self.yticks)
            if self.yticks_labels is not None:
                axes.set_yticklabels(self.yticks_labels, **asdict(self.yticks_format))
