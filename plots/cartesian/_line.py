from typing import Callable, Optional, Sequence, Tuple
from enum import Enum

import numpy as np
import matplotlib.pyplot as plt

from ._plot_object import PlotObject


class LineType(str, Enum):
    """Line type."""

    SOLID = "-"
    """Solid line marker."""

    DASHED = "--"
    """Dashed line marker."""


class MarkerType(str, Enum):
    """Data point marker symbol."""

    NONE = ""
    """No marker used."""

    CIRCLE = "o"
    """Circle marker."""

    STAR = "*"
    """Star marker."""


class _ErrorBars:
    def __init__(self, data):
        self._data = data


class Line(PlotObject):
    """Line object, can be added to a cartesian plot object."""

    Type = LineType
    Marker = MarkerType

    class ErrorBars:
        """Adds error bars to a line plot."""

        def __init__(self) -> None:
            """Uncallable. Create ErrorBars through the static methods `symmetric` or
            `asymmetric`."""
            raise NotImplementedError

        @property
        def _data(self) -> Sequence[float]:
            raise NotImplementedError

        @staticmethod
        def symmetric(data: Sequence[float]) -> "Line.ErrorBars":
            """Creates error bars from a sequence of floats. Each value denotes the
            symmetric +/- value of each data point in the line."""
            return _ErrorBars(data)

        @staticmethod
        def asymmetric(data: Sequence[Tuple[float, float]]) -> "Line.ErrorBars":
            """Creates error bars from a sequence of float-pairs. Each pair denotes the
            lower and upper error bound, respectively."""
            return _ErrorBars(np.array(data).transpose())

    def __init__(
        self,
        x: Sequence[float],
        y: Optional[Sequence[float]] = None,
        *,
        line_type: "Line.Type" = LineType.SOLID,
        marker_type: "Line.Marker" = MarkerType.NONE,
        label: Optional[str] = None,
    ):
        """
        Args:
            x (Sequence[float]): Horizontal axis values.
            y (Optional[Sequence[float]], optional): Vertical axis values. If None, then
                `x` is used as `y` and `x` is replaced by the value indices of `y`.
                Defaults to None.
            line_type (Line.Type, optional): Defaults to LineType.SOLID.
            marker_type (Line.MarkerType, optional): Defaults to MarkerType.NONE.
            label (Optional[str], optional): If `None`, the line is omitted from the
                legend. Defaults to None.
        """
        self._x = x
        self._x_error = None
        self._y = y
        self._y_error = None
        self._line_type = line_type
        self._marker_type = marker_type
        self._label = label

        if y is None:
            self._y = x
            self._x = np.arange(len(x))

    def _render(self, axes: plt.Axes):
        axes.errorbar(
            self._x,
            self._y,
            self._y_error,
            self._x_error,
            fmt=f"{self._marker_type}{self._line_type}",
            label=self._label,
        )

    def set_x_error_bars(self, error_bars: "Line.ErrorBars"):
        """Adds error bars to the x-values of the data points.

        Args:
            error_bars (Line.ErrorBars): Error bars
        """
        self._x_error = error_bars._data

    def set_y_error_bars(self, error_bars: "Line.ErrorBars"):
        """Adds error bars to the y-values of the data points.

        Args:
            error_bars (Line.ErrorBars): Error bars
        """
        self._y_error = error_bars._data
