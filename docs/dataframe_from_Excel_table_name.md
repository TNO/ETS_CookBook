# DataFrame from Excel table name

## What it does


This function looks up a given table name in an Excel file
and returns a DataFrame containing the values of that table.
Note that if the name does not exist (or is spelled wrongly (it's
case-sensitive), the function will crash).
The optional load_data_only parameter puts values in the table if set to
True (its default value. A False value loads formulas).

## Inputs
### table_name
### Excel_file
### load_data_only

## Output

### DataFrame

## Examples

###

## Tests

###

## Potentials for crash


## Open issues