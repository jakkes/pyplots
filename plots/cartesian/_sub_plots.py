from typing import Tuple
import uuid

import matplotlib.pyplot as plt

import plots


class SubPlots:
    def __init__(
        self,
        rows: int,
        cols: int,
        size: Tuple[int, int] = (6.4, 4.8),
    ):
        self._id = str(uuid.uuid4())
        self._rows = rows
        self._cols = cols
        self._size = size

        self._plots = [
            [plots.cartesian.Plot() for _ in range(cols)] for _ in range(rows)
        ]

    def show(self):
        self._render()
        plt.show()
        self._close()

    def _render(self):
        plt.figure(self._id, figsize=self._size)
        i = 1
        for row in range(self._rows):
            for col in range(self._cols):
                ax = plt.subplot(self._rows, self._cols, i)
                i += 1
                self[row, col]._set_ax(ax)
                self[row, col]._render()

    def _close(self):
        plt.close(self._id)

    def __getitem__(self, rowcol: Tuple[int, int]) -> "plots.cartesian.Plot":
        row, col = rowcol
        return self._plots[row][col]

    def __setitem__(self, rowcol: Tuple[int, int], value: "plots.cartesian.Plot"):
        row, col = rowcol
        self._plots[row][col] = value

    def __delitem__(self, *args, **kwargs):
        raise NotImplementedError
