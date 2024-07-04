# What the i does
# Inputs
# Output
# Examples


``` python

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
    # matplotlib says this should create an Axes, but it actually creates
    # a PolarAxes (which has the attribute set_thetagrids used in the function
    # This sets an issue with MyPy, who thinks that this is an Axes at first
    # because this is what add_subplot says.
    # We might avoid the issue by using two variables, but that might create
    # issues when plotting several spiders on top of each other,
    # so the warning remains (until matplotlib also puts PolarAxes as a
    # possible output type)

    spider_alpha = 0.26
    spider_plot = make_spider_chart(
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

    spider_color = 'dodgerblue'
    series_label = 'GSHC'
    data_values = [0.52, 0.18, 0.29, 0.39, 0.66, 0.42]
    spider_plot = make_spider_chart(
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
    plt.show()

```

# Tests
## Theta labels
This test looks if the function sets the theta labels (around the spider) to
the data labels.