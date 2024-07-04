

# **ETS_CookBook**


This is the documentation the ETS CookBook, which is a collection of useful
Python scripts used across ETS (a research group within TNO) models.
The documentation for each script/function can be found by clicking
on the navigation bar on the left (they are arranged by theme).

## Authors and contact
Omar Usmani [Omar.Usmani@TNO.nl](mailto:Omar.Usmani@TNO.nl)

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

## License

This cookbook is released under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).
All accompanying documentation and manuals are released under the 
[Creative Commons BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/deed.en)

## Repository
The code repository can be found [here](https://github.com/TNO/ETS_CookBook)
The distribution package can be found [here](https://pypi.org/project/ETS-CookBook/)

## Status
This CookBook is a working version that will be updated with new functions
as they are need in various projects.
Functions will be updated as appropriate.
You can contact the authors for bug reports, feature suggestions,
or any questions you might have.

## Goals 
This module was forked from prior work,
most notably from [ChaProEV](https://github.com/TNO/ChaProEV).
The forking is due to the/desire to use the auxiliary functions developed
in these projects in more project needs. 


## Libraries used and licensing
(See requirements.txt file for versions (corresponding to Python 3.11.1, which
is the version used for developping and testing the model))
pip install -r requirements.txt

## Acknowledgements
This CookBook has been developed within multiple projects,
including the following:


<table width=500px frame="none">
<tr>
<td valign="middle" width=100px>
<img src=eu-emblem-low-res.jpg alt="EU emblem" width=100%></td>
<img src=MOPO_logo_main_onwhite.svg width = 12%>
<td valign="middle">This project was partly develop under funding from 
European Climate, 
Infrastructure and Environment Executive Agency under the European Union’s 
HORIZON Research and Innovation Actions under grant agreement N°101095998.</td>
<tr>
</table>

