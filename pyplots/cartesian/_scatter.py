from typing import Sequence

import matplotlib.pyplot as plt
import pyplots
from ._plot_object import PlotObject


class Scatter(PlotObject):
    """Scatter plot object."""

    def __init__(self, x: Sequence[float], y: Sequence[float], s: Sequence[float]):
        """
        Args:
            x (Sequence[float]): x-coordinates of markers.
            y (Sequence[float]): y-coordinates of markers.
            s (Sequence[float]): sizes of markers.
        """
        super().__init__()
        self.__x = x
        self.__y = y
        self.__s = s

    def _render(self, axes: plt.Axes):
        axes.scatter(self.__x, self.__y, self.__s)
