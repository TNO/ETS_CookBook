# Save DataFrame

## What it does



This function saves a pandas DataFrame to a number of
file formats and an output folder that are all specified in a
TOML parameters file (under a [files.dataframe_outputs] heading).

Note that for some file types, you might need to install additional
libraries.

Also note that some formats will be saved into a group file that
can contain several other DataFrames (for example sheets into an Excel
workbook or tables into an SQL database). DataFrame_name will be the
file name if the file format does not use group files. If the format does
use a group file, then DataFrame_name will be used for the sub-elements
(sheets, tables, for example), and groupfile_name will be used for
the file name (you can of course use the same value for both), and will be
unused if the file format does not use group files.

## Inputs
###

## Output

###

## Examples

###

## Tests

###

## Open issues

### XML issues


Bug to fix: XML does not accet a number to start names (or
various case variations of xml), which must currently
be handled by the user (who must avoid these).
Other bug: Removing non-alphanumeric characters in the index does not seem
to work (for xml and stata)

### Unsupported formats

gbq and orc outputs are not currently supported, as gbq is not
a local file format, but a cloud-based one and orc does not seem to work
with pyarrow (at least in Windows).


Note that Pandas has a few more export formats that we skipped
orc is not supported in arrows (ar least on Windows)
https://stackoverflow.com/questions/58822095/no-module-named-pyarrow-orc
gbq is about Google cloud storage, not about local files
https://cloud.google.com/bigquery/docs/introduction
Note that clipboard does not produce a file,
but can still be used locally, so the function supports it.


