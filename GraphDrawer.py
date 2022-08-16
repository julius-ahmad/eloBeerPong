import matplotlib.pyplot as plt
import os
import typing


def chart_plot(data: typing.List[typing.Tuple[float, float]], title: str, x_label: str, y_label: str, label: str):
    """
    Takes any number of data points in the form of a list of tuples (x and y coordinates), and plots the points and
    corresponding line on a chart and saves it to file.

    @param data: list of data points in the form of tuples, with the first entry being the x and the second entry the y
        coordinate.
    @param title: the title of the plot
    @param x_label: the label of the x-axis
    @param y_label: the label of the y-axis
    @param label: the title for each line
    """

    plt.plot([x[0] for x in data], [x[1] for x in data], '-o', markersize=3, label=label)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc="lower left")
    directory = 'rankProgress/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(os.path.join(directory, f'{title}.png'), dpi=300)


def draw_graph(data, name):
    """
    Takes list of tuple data points and plots them in the file ranks

    @param data: list of data points in the form of tuples, with the first entry being the x and the second entry the y
    coordinate.
    @param name: The player name to be added as a label
    """
    chart_plot(data, 'ratings', 'Time', 'Elo Rating', name)
