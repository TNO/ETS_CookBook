
# Make spider chart

## What it does
This draws a spider/radar chart on a matplotlib plot/PolarAxes object.
## Inputs

### spider_plot
This is the plot on which the chart will be drawn.
It needs to be a PolarAxes (matplotlib.projections.polar.PolarAxes).
### series_label
This is a label for your series of data, in the form of a string.
### data_labels
This a list of strings labelling each of your data points.
### data_values
This is a list of floats that contains the values of each of your elements
(how far from the center of the spider they are).
### ticks
This is a list (of floats) of ticks along the spider (they should at least
cover all your data values).
### tick_labels
This is a list of labels corresponding to the ticks above.
The list needs to be of the same length as the one above, with
each element corresponding to the one in the above list.
### spider_color
A string giveing the color name
(see [here](https://matplotlib.org/stable/gallery/color/named_colors.html)
for a list).
### spider_marker
A string to set the markers for each data point. 
See [here](https://matplotlib.org/stable/api/markers_api.html) for options.
### spider_linewidth
A float setting the with o the spider line
### spider_alpha
A float (between 0 and 1) setting the opacity of the spider 
(0=fully transparent, 1=fully opaque)

## Output
This returns a plot (PolarAxes) with the spider chart drawn on it.
Use the same plot/PolarAxesas output as you used for input, so
that you can superpose spiders.

## Examples

### Two spiders

``` python

    series_label = 'SFC'
    data_values = [0.6, 0, 0.26, 0.42, 0.89, 0.77]
    data_labels = ['Mango', 'Mapo', 'Lacrosse', 'Floorball', 'Switch', 'NDS']
    ticks = [0, 0.25, 0.50, 0.75, 1.0]
    tick_labels = ['0%', '25%', '50%', '75%', '100%']
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
        ticks,
        tick_labels,
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
        ticks,
        tick_labels,
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



## Open issues

### Colors outside of matplotlib
Need to add support for colors other than matplotlib (via RGB)