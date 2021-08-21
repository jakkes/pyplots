import os
import plots


def test_save():
    plt = plots.cartesian.Plot()
    line = plots.cartesian.Line(
        [1, 2, 3],
        line_type=plots.cartesian.Line.Type.DASHED,
        marker_type=plots.cartesian.Line.Marker.CIRCLE,
    )
    plt.add_object(line)
    os.makedirs("local/tests/cartesian/test_plots", exist_ok=True)
    plt.save("local/tests/cartesian/test_plots/test_save.png")


def test_two_lines():
    plt = plots.cartesian.Plot(
        legend=True, legend_location=plots.cartesian.Plot.Legend.Location.LOWER_RIGHT
    )
    plt.add_object(
        plots.cartesian.Line(
            [1, 2, 3],
            [1, 4, 9],
            line_type=plots.cartesian.Line.Type.DASHED,
            marker_type=plots.cartesian.Line.Marker.CIRCLE,
            label="Line one",
        )
    )
    plt.add_object(
        plots.cartesian.Line(
            [4, 5, 6],
            [16, 25, 36],
            line_type=plots.cartesian.Line.Type.SOLID,
            marker_type=plots.cartesian.Line.Marker.STAR,
            label="Line two",
        )
    )
    os.makedirs("local/tests/cartesian/test_plots", exist_ok=True)
    plt.save("local/tests/cartesian/test_plots/test_two_lines.png")
