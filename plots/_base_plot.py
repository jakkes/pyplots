import abc
import uuid
from typing import Optional, Tuple, Union

import matplotlib.pyplot as plt

import plots


class BasePlot(abc.ABC):
    """Base class for classes able to render plots."""

    def __init__(
        self,
        size: Tuple[int, int] = (6.4, 4.8),
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
            legend (bool, optional): If True, a legend is displayed. Defaults to False.
            legend_location (Union[Plot.Legend.Location, Tuple[int, int]], optional):
                Determines the location of the legend. Defaults to
                `plots.Legend.Location.BEST`. May also be given in coordinates.
        """
        super().__init__()
        self._size = size
        self._legend = legend
        self._legend_location = legend_location
        
        self._owns_figure = _owns_figure
        self._id: Optional[str] = None
        self._axes: Optional[plt.Axes] = None

    @abc.abstractmethod
    def _render(self, axes: plt.Axes):
        """Renders the content of the plot onto a figure, but does not show it."""
        raise NotImplementedError

    def _pre_render(self, axes: plt.Axes):
        """Called before `_render`."""
        pass

    def _post_render(self, axes: plt.Axes):
        """Called after `_render`."""
        if self._legend:
            axes.legend(loc=self._legend_location)

    def _render_pipeline(self, axes: plt.Axes):
        """Executes the render pipeline."""
        self._pre_render(axes)
        self._render(axes)
        self._post_render(axes)

    @abc.abstractmethod
    def _generate_axes(self) -> plt.Axes:
        """Generates and returns the `plt.Axes` object to be used by the rendering
        pipeline."""
        raise NotImplementedError

    def _set_axes(self, axes: plt.Axes):
        self._axes = axes

    def _get_axes(self) -> plt.Axes:
        if self._axes is None:
            if not self._owns_figure:
                raise AttributeError(
                    f"Attempting to generate figure and axes in a child plot object."
                )

            self._id = str(uuid.uuid4())
            plt.figure(self._id, self._size)
            self._axes = self._generate_axes()
        return self._axes

    def show(self):
        """Renders and then displays the plot."""
        if not self._owns_figure:
            raise AttributeError("Cannot show plot that is part of another figure.")

        self._render_pipeline(self._get_axes())
        plt.show()
        self.close()

    def close(self):
        """Closes the plot."""
        if self._id is not None:
            plt.close(self._id)

    def save(self, path: str):
        """Renders and saves the plot to the given path.

        Args:
            path (str): File path to which the figure should be saved.
        """
        self._render_pipeline(self._get_axes())
        plt.savefig(path)
        self.close()