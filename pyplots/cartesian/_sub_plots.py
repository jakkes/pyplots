from typing import Iterator, Tuple, Union
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

    Alternatively, subplots are accessed by their single row-major ordered index:
    ```python
    subplots = SubPlots(2, 2)
    upper_left = subplots[0]
    upper_right = subplots[1]
    lower_left = subplots[2]
    lower_right = subplots[3]
    ```
    """

    def __init__(
        self,
        rows: int,
        cols: int,
        size: Tuple[int, int] = (6.4, 4.8),
        sharex: bool = False,
        sharey: bool = False,
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
            sharex (bool): If `True`, all plots use the same range on the x-axis.
                Defaults to `False`.
            sharey (bool): If `True`, all plots use the same range on the y-axis.
                Defaults to `False`.
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
        self.__rows = rows
        self.__cols = cols
        self.sharex = sharex
        """If `True`, all subplots use the same x-axis range."""

        self.sharey = sharey
        """If `True`, all subplots use the same y-axis range."""

        self.__plots = [
            [pyplots.cartesian.Plot(_owns_figure=False) for _ in range(cols)]
            for _ in range(rows)
        ]

    @property
    def rows(self) -> int:
        """Number of rows in the subplot."""
        return self.__rows

    @property
    def cols(self) -> int:
        """Number of columns in the subplot."""
        return self.__cols

    def _generate_axes(self) -> plt.Axes:
        return [
            [
                plt.subplot(
                    self.__rows,
                    self.__cols,
                    1 + col + self.__cols * row,
                )
                for col in range(self.__cols)
            ]
            for row in range(self.__rows)
        ]

    def _render(self, axes: plt.Axes):
        for row in range(self.__rows):
            for col in range(self.__cols):
                self[row, col]._render_pipeline(axes[row][col])

    def _post_render(self, axes: plt.Axes):
        super()._post_render(axes)
        if self.sharex:
            self._set_shared_x(axes)
        if self.sharey:
            self._set_shared_y(axes)

    def _set_shared_x(self, axes: plt.Axes):
        min_x, max_x = None, None
        for row in range(self.__rows):
            for col in range(self.__cols):
                if min_x is None:
                    min_x, max_x, _, _ = axes[row][col].axis()
                else:
                    xlow, xhigh, _, _ = axes[row][col].axis()
                    min_x = min(xlow, min_x)
                    max_x = max(xhigh, max_x)
        for row in range(self.__rows):
            for col in range(self.__cols):
                axes[row][col].set(xlim=(min_x, max_x))

    def _set_shared_y(self, axes: plt.Axes):
        min_y, max_y = None, None
        for row in range(self.__rows):
            for col in range(self.__cols):
                if min_y is None:
                    _, _, min_y, max_y = axes[row][col].axis()
                else:
                    _, _, ylow, yhigh = axes[row][col].axis()
                    min_y = min(ylow, min_y)
                    max_y = max(yhigh, max_y)
        for row in range(self.__rows):
            for col in range(self.__cols):
                axes[row][col].set(ylim=(min_y, max_y))

    def __getitem__(self, rowcol: Union[int, Tuple[int, int]]) -> "pyplots.cartesian.Plot":
        if type(rowcol) is tuple:
            row, col = rowcol
            return self.__plots[row][col]
        else:
            return self[rowcol // self.__cols, rowcol % self.__cols]

    def __iter__(self) -> Iterator["pyplots.cartesian.Plot"]:
        for i in range(self.__rows * self.__cols):
            yield self[i]
