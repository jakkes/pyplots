from enum import Enum


class Font:
    """Font options."""

    class Family(str, Enum):
        """Font family."""
        SERIF = "serif"
        SANS_SERIF = "sans-serif"
        CURSIVE = "cursive"
        FANTASY = "fantasy"
        MONOSPACE = "monospace"

    class Style(str, Enum):
        NORMAL = "normal"
        ITALIC = "italic"
        OBLIQUE = "oblique"
