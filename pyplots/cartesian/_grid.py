import matplotlib.pyplot as plt
import numpy as np

from ._plot_object import PlotObject


class Grid(PlotObject):
    """Grid object, used to plot a grid or image.
    """

    def __init__(self, values: np.ndarray):
        """
        Args:
            values (np.ndarray): Two dimensional array of values.
        """
        super().__init__()
        if len(values.shape) != 2:
            raise ValueError("Values must be a two dimensional array.")
        self._values = values


    def _render(self, axes: plt.Axes):
        axes.imshow(self._values)
