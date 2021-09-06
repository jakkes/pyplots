from typing import Any, Dict, Optional, Sequence, Tuple, Union
from enum import Enum

import numpy as np
import matplotlib.pyplot as plt

import pyplots
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

    class ErrorBars:
        """Adds error bars to a line plot."""

        def __init__(
            self,
            x_error: Union[Sequence[float], Sequence[Tuple[float, float]]]=None,
            y_error: Union[Sequence[float], Sequence[Tuple[float, float]]]=None,
        ) -> None:
            """
            Args:
                x_error (Union[Sequence[float], Sequence[Tuple[float, float]]],
                    optional): Error of x-values. If None, no error bars are added. If a
                    sequence of floats, then these values are treated as symmetric +/-
                    errors. If a sequence of float-pairs, these denote the lower and
                    upper bounds respectively. Defaults to None.
                y_error (Union[Sequence[float], Sequence[Tuple[float, float]]],
                    optional): Error of y-values. See format help on `x_values`.
            """
            self._x_error = np.array(x_error).transpose()
            self._y_error = np.array(y_error).transpose()

        def _get_kwargs(self) -> Dict[str, Any]:
            return {
                "xerr": self._x_error,
                "yerr": self._y_error
            }

    def __init__(
        self,
        x: Sequence[float],
        y: Optional[Sequence[float]] = None,
        *,
        color: Optional[Union[pyplots.Color, str]] = None,
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
            color (Optional[Union[pyplots.Color, str]], optional): Color in which the plot
                is rendered, either as a pre-defined color or in hex color code. If
                `None`, then the color is selected automatically from the default color
                cycle.
            line_type (Line.Type, optional): Defaults to LineType.SOLID.
            marker_type (Line.MarkerType, optional): Defaults to MarkerType.NONE.
            label (Optional[str], optional): If `None`, the line is omitted from the
                legend. Defaults to None.
        """
        self._x = x
        self._y = y
        self._error = None
        self._color = color
        self._line_type = line_type
        self._marker_type = marker_type
        self._label = label

        if y is None:
            self._y = x
            self._x = np.arange(len(x))

    def _render(self, axes: plt.Axes):
        error_kwargs = {} if self._error is None else self._error._get_kwargs()
        
        axes.errorbar(
            self._x,
            self._y,
            fmt=f"{self._marker_type}{self._line_type}",
            color=self._color,
            label=self._label,
            **error_kwargs
        )

    def error_bars(self, error_bars: "Line.ErrorBars"):
        """Adds error bars to the x-values of the data points.

        Args:
            error_bars (Line.ErrorBars): Error bars
        """
        self._error = error_bars
