from typing import Optional, Sequence
from enum import Enum


class LineType(Enum):
    """Line type enumeration."""
    SOLID = 0
    DASHED = 1
    DOTTED = 2


class MarkerType(Enum):
    """Line marker type enumeration."""
    NONE = 0
    CIRCLE = 1
    STAR = 2


class Line:
    """Line object, can be added to a cartesian plot object."""

    Type = LineType
    MarkerType = MarkerType

    def __init__(
        self,
        x: Sequence[float],
        y: Optional[Sequence[float]] = None,
        line_type: "Line.Type" = LineType.SOLID,
        marker_type: "Line.MarkerType" = MarkerType.NONE,
        label: Optional[str] = None
    ):
        """
        Args:
            x (Sequence[float]): [description]
            y (Optional[Sequence[float]], optional): [description]. Defaults to None.
            line_type (Line.Type, optional): [description]. Defaults to LineType.SOLID.
            marker_type (Line.MarkerType, optional): [description]. Defaults to MarkerType.NONE.
            label (Optional[str], optional): [description]. Defaults to None.
        """
        self._x = x
        self._y = y
        self._line_type = line_type
        self._marker_type = marker_type
        self._label = label
