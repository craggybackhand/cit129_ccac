# Using capital_projects.py

Capital_projects.py is a filter script that reads the capital_projects.csv file downloaded from https://data.wprdc.org/dataset/capital-projects.

To use it, you must create a "filter.json" file in the same directory as the script. This json will contain filter values in the following format:

`{"fiscal_year": "2017", "start_date": "2017-02-08", "area": "", "asset_type": "Bridge", "planning_status": "Completed"}`

If you run the script, it will take these filter values as input and return all project IDs that match the filter. If you run it in the format listed
above, it will return values for two different capital projects. 

You can alter the value fields of each .json object to change the contents of the filter as desired. Any empty values will be ignored and will not
impact the filtering.
