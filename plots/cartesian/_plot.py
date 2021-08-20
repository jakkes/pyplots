from typing import Tuple
import uuid

import matplotlib.pyplot as plt


class Plot:
    """Figure with a single plot of cartesian axes."""
    def __init__(
        self, size: Tuple[int, int] = (6.4, 4.8), logy: bool = False, logx: bool = False
    ):
        """
        Args:
            size (Tuple[int, int], optional): Size of the figure in inches,
                `(width, height)`. Defaults to (6.4, 4.8).
            logy (bool, optional): If True, the y-axis is logarithmic. Defaults to
                False.
            logx (bool, optional): If True, the x-axis is logarithmic. Defaults to
                False.
        """
        self._id = str(uuid.uuid4())
        self._logy = logy
        self._logx = logx

        self._fig, self._ax = plt.figure(self._id, figsize=size)

    def add_line(self):
        pass
