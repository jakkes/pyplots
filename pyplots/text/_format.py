from dataclasses import dataclass
from ._font import Font
from ._alignment import Alignment

import pyplots


@dataclass
class Format:
    """Configuration for texts."""
    
    alpha: float = None

    backgroundcolor: pyplots.Color = pyplots.Color.WHITE

    color: pyplots.Color = pyplots.Color.BLACK

    fontsize: float = 12

    fontstyle: "pyplots.text.Font.Style" = Font.Style.NORMAL

    fontfamily: "pyplots.text.Font.Family" = Font.Family.SERIF

    horizontalalignment: "pyplots.text.Alignment" = Alignment.CENTER

    linespacing: float = 1.0

    rotation: float = 0.0
