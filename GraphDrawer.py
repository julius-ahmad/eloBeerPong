import matplotlib.pyplot as plt
import os
import typing


def chart_plot(data: typing.List[typing.Tuple[float, float]], title: str, x_label: str, y_label: str):
    """
    Takes any number of data points in the form of a list of tuples (x and y coordinates), and plots the points and
    corresponding line on a chart and saves it to file.

    @param data: list of data points in the form of tuples, with the first entry being the x and the second entry the y
        coordinate.
    @param title: the title of the plot
    @param x_label: the label of the x-axis
    @param y_label: the label of the y-axis
    """

    plt.plot([x[0] for x in data], [x[1] for x in data], '-o', markersize=3)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    directory = 'rankProgress/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(os.path.join(directory, f'{title}.png'), dpi=300)


def draw_graph(data):
    """
    Takes list of tuple data points and plots them in the file ranks

    @param data: list of data points in the form of tuples, with the first entry being the x and the second entry the y
        coordinate.
    """
    chart_plot(data, 'ranks', 'Time', 'ELO rating')
