from enum import Enum


class Legend:

    class Location(str, Enum):
        """Location of the legend."""
        BEST = "best"
        UPPER_LEFT = "upper left"
        UPPER_CENTER = "upper center"
        UPPER_RIGHT = "upper right"
        CENTER_LEFT = "center left"
        CENTER = "center"
        CENTER_RIGHT = "center right"
        LOWER_LEFT = "lower left"
        LOWER_CENTER = "lower center"
        LOWER_RIGHT = "lower right"
