import abc
import matplotlib.pyplot as plt


class PlotObject(abc.ABC):

    @abc.abstractmethod
    def _render(self, axes: plt.Axes):
        raise NotImplementedError
