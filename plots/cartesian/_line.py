from typing import Callable, Optional, Sequence
from enum import Enum

import numpy as np

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


class Line(PlotObject):
    """Line object, can be added to a cartesian plot object."""

    Type = LineType
    Marker = MarkerType

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
        self._y = y
        self._line_type = line_type
        self._marker_type = marker_type
        self._label = label

        if y is None:
            self._y = x
            self._x = np.arange(len(x))

    def _render(self, plot_fn: Callable):
        plot_fn(
            self._x, self._y, f"{self._marker_type}{self._line_type}", label=self._label
        )
