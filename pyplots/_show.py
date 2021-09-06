import matplotlib.pyplot as plt

import pyplots


def show(*plots: pyplots.BasePlot):
    """Renders and displays a set of plots. This method will block until all plot
    windows have been manually closed.

    Args:
        plots (pyplots.BasePlot): Sequence of plots to display.
    """
    for plot in plots:
        plot._render_pipeline(plot._get_axes())
    plt.show()
    for plot in plots:
        plot.close()
