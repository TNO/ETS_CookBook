
# Make spider chart

## What it does
## Inputs
## Output
## Examples


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
    spider_figure.savefig('docs/spider_example.png')


```

![Spider example should be here](spider_example.png 'An example of a spider chart')

Note that we use spider_plot as both input and output of make_spider_chart.
We do this so that we can plot two spiders on top of each other (by calling
the function twice).

## Tests
### Theta labels
This test looks if the function sets the theta labels (around the spider) to
the data labels.

## Typing issues

### Axes versus PolarAxes
You might encounter an issue when running a MyPy (or other) type check.
This comes from this line:
``` python
 spider_plot.set_thetagrids(angles * 180 / np.pi, data_labels)
```
This puts the data labels as the theta labels (around the spider) requires
spider_plot to be a PolarAxes (matplotlib.projecions.polar.PolarAxes) element
because set_thetagrids is an attribute of PolarAxes (and not Axes).

The problem is that the functions used to create a plot (an Axes element) claim
to only create Axes, even if they create a PolarAxes, such as with the line below:
``` python
spider_plot = spider_figure.add_subplot(111, polar=True)
```
Matplotlib claims that add_subplot creates an Axes object, but the result
is a PolarAxes. This means that a type check (such as MyPy) might throw an
error. This might be solved if matplotlib updates its typing documentation
by adding the possibility that add_subplot can also create a PolarAxes.