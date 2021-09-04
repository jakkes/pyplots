from enum import Enum
from typing import List

import matplotlib


class Color(str, Enum):
    """Set of predefined colors."""

    MATPLOT_BLUE = "#1f77b4"
    """Default blue of the matplotlib color cycle."""

    @staticmethod
    def get_default_color_cycle() -> List[str]:
        return ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
