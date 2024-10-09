# Register color bars

## What it does
This function reads the user-defined color bars in a parameter file
(names for the bars, and a list of the colors they contain, with the
first being at the bottom of the bar, and the last at the top, and the
others in between). It then creates the color bars and stores them
in the list of available color maps.

``` python

    color_bars = parameters['color_bars']

    # This dictionary stores the dictionaries for each color bar
    color_bar_dictionary: dict = {}
    # These colors are the three base keys of each bar color dictionary
    # Each dictionary contains a tuple of tuples for each base colors
    # Each of these sub-tuples cotains a step (between 0 and 1),
    # and a tone of the basic color in question (red, green, or blue)
    # This is repeated. The second value can be different
    # if cretaing discontinuities.
    # See https://matplotlib.org/stable/gallery/color/custom_cmap.html
    # for details
    base_colors_for_color_bar = ['red', 'green', 'blue']

    # We fill the color bar dictionary
    for color_bar in color_bars:
        # We read the color list
        color_bar_colors = color_bars[color_bar]
        # We set the color steps, based on the color list
        color_steps = np.linspace(0, 1, len(color_bar_colors))

        color_bar_dictionary[color_bar] = {}
        for base_color_index, base_color in enumerate(
            base_colors_for_color_bar
        ):
            # We create a list of entries for that base color
            # It is a list so that we can append,
            # but we will need to convert it to a tuple
            base_color_entries = []
            for color_bar_index, (color_step, color_bar_color) in enumerate(
                zip(color_steps, color_bar_colors)
            ):
                # We get the ton by getting the RGB values of the
                # color bar color and taking the corresponding base index
                color_bar_color_tone = get_rgb_from_name(
                    color_bar_color, parameters
                )[base_color_index]

                base_color_entries.append(
                    # The subtuples consist of the color step
                    (
                        color_step,
                        # And the tone of the base color
                        # for the color corresponding
                        # to the step
                        color_bar_color_tone,
                        # This iis repeated for continuous schemes
                        # See
                        # https://matplotlib.org/stable/gallery/color/custom_cmap.html
                        # for details
                        color_bar_color_tone,
                    )
                )
            # We now convert the list to a tuple and put it into
            # the dictionary
            color_bar_dictionary[color_bar][base_color] = tuple(
                base_color_entries
            )

    # We now add the color bars to the color maps

    for color_bar in color_bars:
        color_bar_to_register = matplotlib.colors.LinearSegmentedColormap(
            color_bar, color_bar_dictionary[color_bar]
        )

        if color_bar_to_register.name not in matplotlib.pyplot.colormaps():
            matplotlib.colormaps.register(color_bar_to_register)

```

## Inputs
###

## Output

###

## Examples

###

## Tests

###


## Open issues
