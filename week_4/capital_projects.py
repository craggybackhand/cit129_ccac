# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:54:57 2020

@author: joel.whiteman
"""

import json
import csv

def csv_reader(filter_dict):
    """
    Opens and reads a csv object and then applies filters to it.
    """
    with open ("capital_projects.csv", "r", newline='') as csv_reader:   
        reader = csv.DictReader(csv_reader)
        for project_row in reader:
            aggregated_filter(project_row, filter_dict)

def filter_reader():
    """
    Reads a json-encoded filter and turns it into a filter_dict object.
    """
    with open ('filter.json', "r") as filter_file:
        filter_dict = json.load(filter_file)
    return filter_dict

def aggregated_filter(project_row, filter_dict):
    """
    Runs a series of filters on a project row taken in while looping over a .csv.
    """
    if fiscal_year_filter(project_row, filter_dict["fiscal_year"]):
        if start_date_filter(project_row, filter_dict["start_date"]):
            if area_filter(project_row, filter_dict["area"]):
                print(project_row["asset_id"])

def fiscal_year_filter(project_row, fiscal_year_criteria):
    """
    Takes in project_rows from a csv loop and checks the fiscal_year for a criterion.
    """
    if project_row['fiscal_year'] == fiscal_year_criteria:
        return project_row
    else:
        return None

def start_date_filter(project_row, start_date_criteria):
    """
    Takes in project_rows from a csv loop and checks the start_date field for a criterion.
    """
    if project_row['start_date'] == start_date_criteria:
        return project_row
    else:
        return None
    
def area_filter(project_row, area_criteria):
    """
    Takes in project_rows from a csv loop and checks the area field for a criterion.
    """
    if project_row['area'] == area_criteria:
        return project_row
    else:
        return None

def main():
    filter_dict = filter_reader()
    csv_reader(filter_dict)

if __name__ == "__main__":
    main()