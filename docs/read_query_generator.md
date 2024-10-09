# Read query geerator

## What it does
This function returns an sql read/select query string that can be used
(for example) in Panda's read_sql.
    - query_filter_values: The comparison values used for the filter.
    The three special cases are:
        1) Like: This needs to be a double quote string (since it will be
        nested into a single-quote string) with percentage signs,
        such as '"%2020-05-08%"' for timestamps for May 8th, 2020
        2) Between: Provide the two  values  into a
        list. If the values arte strings that contain spaces,
        you need nested quotes, such as:
        ['"2020-05-08 00:00:00"','"2020-06-26 16:00:00"']
        3) In provide the two tuple values into a list.,
        e.g: [(52.1,4.9),(52.0,5.1)]


## Inputs
### quantities_to_display
 A string list of table column names
(as strings, in
single quotes), separated by commas. If the user
wants all columns displayed, then they should use a '*'. If one (or more)
of the column names have spaces, then the user needs to use f strings and
double quotes, as in the following example:
``` python
quantity_1 = 'Time'
quantity_2 =  'Surveyed Area'
quantity_2_with_quotes = f'"quantity_2"'
quantities_to_display = f'{quantity_1}, {quantity_2_with_quotes}'
```
This latter variable is the input for the function.

### source_table
A string that 
 is the name of the source table. Note that it has a similar
need if the name has spaces, so use:
``` python
source_table = f'"My Table"' 
```
as an input.

### query_filter_quantities:
A list of strings each representing a column
name the user wants to filter. Again, names with spaces require
f-strings and double quotes, so add:
``` python
f'"Surveyed Area"'
```
to your list of filter names.

### query_filter_types

This list of strings (the list has to be the same length as the
above list of quantities)
says which filter to use. Currently supported options are:


- '='       (equal to)
- '<'       (smaller than)
- '>'       (larger than)
- '!='      (not equal)
- '<>'      (not equal)
- '<='      (smalller or equal)
- '>='      (larger or equal)
- 'like'      (matches/ searches for a pattern)
- 'between'   (between two  values)
- 'in'        (to select multiple values for one or several columns)


### query_filter_values
A list of strings (the length of the list needs to be the same as the above two)
containing comparison values used for the filter.
The three special cases are:
    1) Like: This needs to be a double quote string (since it will be
    nested into a single-quote string) with percentage signs,
    such as '"%2020-05-08%"' for timestamps for May 8th, 2020
    2) Between: Provide the two  values  into a
    list. If the values arte strings that contain spaces,
    you need nested quotes, such as:
    ['"2020-05-08 00:00:00"','"2020-06-26 16:00:00"']
    3) In provide the two tuple values into a list.,
    e.g: [(52.1,4.9),(52.0,5.1)]



## Output

###

## Examples

###

## Tests

###

## Open issues

### Add default lists with empty strings