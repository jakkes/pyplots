from typing import Tuple, Union
import uuid

import matplotlib.pyplot as plt

import pyplots


class SubPlots(pyplots.BasePlot):
    """Figure containing multiple subplots of cartesian axes.
    
    A subplot may be accessed by its row and column:
    ```python
    subplots = SubPlots(2, 2)
    upper_left = subplots[0, 0]
    upper_right = subplots[0, 1]
    lower_left = subplots[1, 0]
    lower_right = subplots[1, 1]
    ```
    
    These may then be treated as a `pyplots.cartesian.Plot`, which is their true type.
    """

    def __init__(
        self,
        rows: int,
        cols: int,
        size: Tuple[int, int] = (6.4, 4.8),
        legend: bool = False,
        legend_location: Union[
            "pyplots.Legend.Location", Tuple[int, int]
        ] = pyplots.Legend.Location.BEST,
        _owns_figure: bool = True,
    ):
        """
        Args:
            rows (int): Number of rows.
            cols (int): Number of columns.
            size (Tuple[int, int], optional):Size of the figure in inches,
                `(width, height)`. Defaults to (6.4, 4.8).
            legend (bool, optional): If True, a legend is displayed. Defaults to False.
            legend_location (Union[Plot.Legend.Location, Tuple[int, int]], optional):
                Determines the location of the legend. Defaults to
                `pyplots.Legend.Location.BEST`. May also be given in coordinates.
        """
        super().__init__(
            size=size,
            legend=legend,
            legend_location=legend_location,
            _owns_figure=_owns_figure,
        )
        self.rows = rows
        self.cols = cols

        self.__plots = [
            [pyplots.cartesian.Plot(_owns_figure=False) for _ in range(cols)]
            for _ in range(rows)
        ]

    def _generate_axes(self) -> plt.Axes:
        return [
            [
                plt.subplot(self.rows, self.cols, 1 + col + self.cols * row)
                for col in range(self.cols)
            ]
            for row in range(self.rows)
        ]

    def _render(self, axes: plt.Axes):
        for row in range(self.rows):
            for col in range(self.cols):
                self[row, col]._render_pipeline(axes[row][col])

    def __getitem__(self, rowcol: Tuple[int, int]) -> "pyplots.cartesian.Plot":
        row, col = rowcol
        return self.__plots[row][col]
