# Type hinting here seems to create issues
# Either with MyPy complaining about imports mising attributes
# or MyPy not working
import matplotlib.pyplot as plt

import ETS_CookBook as cook


def test_theta_labels_setting():
    '''
    This tests if the theta labels have actually been set to the chosen
    data labels.
    '''
    series_label = 'SFC'
    data_values = [0.6, 0, 0.26, 0.42, 0.89, 0.77]
    data_labels = ['Mango', 'Mapo', 'Lacrosse', 'Floorball', 'Switch', 'NDS']
    markers = [0, 0.25, 0.50, 0.75, 1.0]
    marker_labels = ['0%', '25%', '50%', '75%', '100%']
    spider_color = 'fuchsia'
    spider_marker = 'o'
    spider_linewidth = 2

    spider_figure = plt.figure()
    spider_plot = spider_figure.add_subplot(111, polar=True)
    series_label = 'SFC'
    data_values = [0.6, 0, 0.26, 0.42, 0.89, 0.77]
    data_labels = ['Mango', 'Mapo', 'Lacrosse', 'Floorball', 'Switch', 'NDS']
    markers = [0, 0.25, 0.50, 0.75, 1.0]
    marker_labels = ['0%', '25%', '50%', '75%', '100%']
    spider_color = 'fuchsia'
    spider_marker = 'o'
    spider_linewidth = 2

    spider_figure = plt.figure()
    spider_plot = spider_figure.add_subplot(111, polar=True)

    spider_alpha = 0.26
    spider_plot = cook.make_spider_chart(
        spider_plot,
        series_label,
        data_labels,
        data_values,
        markers,
        marker_labels,
        spider_color,
        spider_marker,
        spider_linewidth,
        spider_alpha,
    )

    theta_axis_labels = [
        grid_element.get_text() for grid_element in plt.thetagrids()[1]
    ]

    assert theta_axis_labels == data_labels
