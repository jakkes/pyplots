import abc
from typing import Callable


class PlotObject(abc.ABC):

    @abc.abstractmethod
    def _render(self, plot_fn: Callable):
        raise NotImplementedError
