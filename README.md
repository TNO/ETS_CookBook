# **ETS_CookBook**




This repository contains the ETS CookBook, which is a collection of useful
Python scripts used across ETS (a research group within TNO) models.


## Goals 
This module was forked from prior work,
most notably from [ChaProEV](https://github.com/TNO/ChaProEV).
The forking is due to the need/desire to use the auxiliary functions developed
in these projects in more projects. 


## Authors and contact
Omar Usmani (Omar.Usmani@TNO.nl)

## Installation and use
You can either copy the ETS_CookBook.py file (in src/ETS_CookBook) to your
project and import it, or (preferably) install it via PyPi:

``
pip install ETS_CookBook
``

You also need to ensure that all the required libraries are installed. Their
list in given in requirements.txt.
You can do this with the following command:

``
pip install -r requirements.txt
``

To use the CookBook, import it as such:
``
from ETS_CookBook import ETS_CookBook as cook
``
Then you can call your functions as such:
``
cook.reference_scale([0.26, 0.89])
``

(You can replace the as cook with something else, or even skip it altogether:
if you do skip it, then call the functions with ETS_CookBook.function).

## Licence

This cookbook is released under the Apache 2.0 licence.
All accompanying documentation and manual are released under the 
Creative Commons BY-SA 4.0 license.


## Status
This CookBook is a working version that will be updated with new functions
as they are neeed in various projects.
Functions will be updated as appropriate.
You can contact the authors foor bug reports, fetaure suggestions,
or any questions you might have.

## Libraries used and licensing
(See requirements.txt file for versions (corresponding to Python 3.11.1, which
is the version used for developping  and testing the model))
pip install -r requirements.txt

## Included scripts/functions



1. **check_if_folder_exists:** Checks if a folder exists.
    If it does not, it creates it.
2. **parameters_from_TOML:**  Reads a TOML parameters file name and returns
    a parameters dictionary.
3. **reference_scale:** This function takes a list of numbers an returns
    a scale (lower and upper boundary) they are in.
4. **dataframe_from_Excel_table_name:** This function looks up a given table
    name in an Excel file and returns a DataFrame containing the values of
    that table.
5. **dataframe_to_Excel:** This function takes a DataFrame and puts it into
    a new sheet in an Excel workbook.
6. **get_extra_colors:** This function gets the user-defined extra colors
    from a file.
7. **get_RGB_from_name:** This function takes a color name and returns
    its RGB values (0 to 1).
8. **rgb_color_list:** Gets a list of RGB codes for a list of color names.
9. **register_color_bars:** This function reads the user-defined color bars
    in a parameter file, creates them and makes them available.
10. **get_season:** This function takes a datetime timestamp and tells us
    in which season it is.
11. **save_figure:** Saves a Matplotlib figure to a number of file formats set
    by the user.
12. **save_dataframe:** Saves a pandas dataframe to a number of file formats
    set by the user.
13. **put_dataframe_in_sql_in_chunks:** This function takes a Dataframe and
    writes it into the table of an SQL database.
    It does so in chunks to avoid memory issues.
14. **query_list_from_file:** This returns a list of queries from an SQL file
15. **dataframes_from_query_list:**This returns a list of dataframes,
    each obtained from a query in the list
16. **from_grib_to_dataframe:**
This function takes a grib file and converts it to a DataFrame.
17. **read_query_generator:** This function returns an sql query string that
    can be used (for example) in Panda's read_sql.
18. **database_tables_columns:** Returns a dictionary with the tables of a
    database as keys and their columns as values.
19. **download_and_save_file:** Downloads a file from an URL and saves it
20. **string_to_float:** Converts strings to floats,
    and to zero if the string is not a float.
21. **get_map_area_data:** Gets area data into a Dataframe
22. **get_map_borders_data:** Gets borders data into a Dataframe
23. **get_map_points_data:** Gets points data into a Dataframe
24. **make_spider__chart:** Makes a spider/radar chart
25. **update_database_table:**
    This function updates the values
    of one row of a table in a database.
    If you want to change multiple rows (with
    a different value for each row), then you need to iterate over the rows.
26. **update_database_table:** Returns a query filter stringthat can be used
in an SQL query.
27. **read_table_from_database:** Returns a table from a database
in an SQL query.
28. **put_dataframe_in_word_document:** Puts a DataFrame in a Word document
29. **make_cell_text_vertical:**: Changes the orientation of a Word table cell
to vertical

## Acknowledgements
This CookBook has been developed within multiple projects,
including the following:





<table width=500px frame="none">
<tr>
<td valign="middle" width=100px>
<img src=eu-emblem-low-res.jpg alt="EU emblem" width=100%></td>
<img src=MOPO_logo_main.svg width = 12%>
<td valign="middle">This project was partly develop under funding from 
European Climate, 
Infrastructure and Environment Executive Agency under the European Union’s 
HORIZON Research and Innovation Actions under grant agreement N°101095998.</td>
<tr>
</table>


