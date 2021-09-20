from enum import Enum


class Alignment(str, Enum):
    """Text alignment."""
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
