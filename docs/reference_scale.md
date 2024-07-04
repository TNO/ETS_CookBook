# Reference scale

## What it does

This function takes a list of numbers and returns a scale
(lower and upper boundary) they are in.
The digit shift parameter tells us on which digit we need to
focus. The default is 0, so the upper boundary of 53.57 will be 60
by default, but 54 if the digit shift is 1 (thus focussing on the 3 part).
This can for example be useful to determine the plotting area of a dataset
(x-axis boundaries).

### Error avoidance

## Inputs
### number_list
A list of floats
### digit_shift
An integer that ....
The default value is 0.

## Output

### Reference scale
A list of two floats that .....

## Examples

###

## Tests

### Basic test

### digit shift test

### With zero as a boundary

### With negatives


### Zero error avoidance


## Open issues



