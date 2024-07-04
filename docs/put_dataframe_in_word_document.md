# Put DataFrame in Word document

## What it does
 This function puts a Dataframe into a given Word document.
If the document does not exist, it is created.
You can also optionally specify number formats for each column (in a list).
If you do not provide the same amount of formats as there are columns
in your DataFrame, then only the first one will be used across all columns.
If you don't provide any format list, then the default is that your numbers
will be displayed with two decimals.
You can also provide a table format.
Note that the table style must exist in the document for you to be able to
use it (so make document, put a table in it with the style you
want, and delete the table before saving). If it does not, you can use the
defaults listed here:
https://python-docx.readthedocs.io/en/latest/user/styles-understanding.html
or simply omit the style argument.
You can also indicate which code you want to use for empty values
(the default is an empty string)
Identical headers are merged by default and merged rows have their text
flipped by default (you can also change the default
bottom to top flip).


## Inputs
###

## Output

###

## Examples

###

## Tests

###

## Open issues