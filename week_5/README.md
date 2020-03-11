# Using apicall.py

apicall.py is a script that calls the Rebrickable API documented at https://rebrickable.com/api/v3/docs/?key=

To use it, you need a newline-delimited text file named years.txt. This file should contain a list of years you want to query the API for, with
one year on each line. The years.txt file in this directory serves as a functional example.

When you run the script, it will call the Rebrickable API and return information about the average number of pieces used in Lego sets released 
during the years you gave as input. The script will output a file named lego_averages.csv with the resulting information. The lego_averages.csv
file in this repos is an example of this ouput. 

Please note that if you input an year with no information or an invalid string (i.e. a text string), the script will still run on the other years
and simply mark those strings as invalid in the output.


