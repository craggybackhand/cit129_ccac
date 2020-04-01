# Using import_test.py

**import_test.py** is a basic scraping script that pulls the names of lego sets within given categories from [Brickset pages like this one](https://brickset.com/sets/theme-City/year-2020).

Currently, its functionaliy is relatively limited and it only pulls data on sets from 2020. 

To use it, you must create a newline-delimited list of categories that you'd like to pull information about. The file **categories.txt** in this directory is an example of what an input file should look like. You can find a list of compatible 2020 Lego sets at [this link](https://brickset.com/browse/sets). 

To run the script, you must provide the path of your input file with the argument -i. For example, to run it on **categories.txt**, you would run

`python import_test.py -i categories.txt`
