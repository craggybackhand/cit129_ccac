# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:54:57 2020
@author: joel.whiteman
"""

import os
import json
import csv

def filter_reader():
    """
    Reads a json-encoded filter and turns it into a filter_dict object.

    This function constructs a filter dictionary from the user-provided .json filter object. It
    reads the filter.json file and turns it into an OrderedDict object which is then returned.
    """
    with open ('filter.json', "r") as filter_file:
        filter_dict = json.load(filter_file)
    return filter_dict

def csv_reader(filter_dict):
    """
    Opens and reads a csv object and then applies filters to it. Writes the output to a file.
    
    This function controls most of the filtering and output logic of the program. It first opens
    a .csv and reads it into an OrderedDict object. It then iterates over the "rows" in the
    dictionary object, passing them into the aggregated_filter function along with a matching_list
    object that will be written by the filter. Once the filter has run on each row, it calls
    write_output to write all of the objects in the matching_list to a file.
    """
    matching_list = []
    with open ("capital_projects.csv", "r", newline='') as csv_reader:   
        reader = csv.DictReader(csv_reader)
        for project_row in reader:
            aggregated_filter(project_row, filter_dict, matching_list)
    write_output(matching_list) 

def aggregated_filter(project_row, filter_dict, matching_list):
    """
    Runs a nested series of filters on a project row taken in while looping over a .csv.

    This function calls the various filters that are applied based on the content of the
    filter_dict object. Each filter is called in succession, with the .csv "row" from the csv
    reader object and the appropriate field from the filter_dict being passed in. The filters
    are nested such that the later filters only run on items that match the earlier ones. If 
    every filter returns the project_row (meaning each filter has matched the filter criteria or
    some filter fields were empty in the filter_dict and thus not being used to filter), the 
    project_row id value is written to the matching_list object that has been passed into 
    the function.
    """
    if fiscal_year_filter(project_row, filter_dict["fiscal_year"]):
        if start_date_filter(project_row, filter_dict["start_date"]):
            if area_filter(project_row, filter_dict["area"]):
                if asset_type_filter(project_row, filter_dict["asset_type"]):
                    if planning_status_filter(project_row, filter_dict["planning_status"]):
                        matching_list.append(project_row["id"])

def fiscal_year_filter(project_row, fiscal_year_criteria):
    """
    Takes in project_rows from a .csv loop and checks the fiscal_year for a criterion.

    This is one of several filter functions that runs on individual project rows from the .csv
    dictionary object. This one takes in the "fiscal_year" field from the filter_dict as
    fiscal_year_criteria. It checks if the filter field is empty. If it is not, it then checks
    if the relevant contents of the .csv object matches the filter field. If the filter field is
    empty or matches the contents of the relevant field in the .csv project_row, it returns the 
    project_row. Otherwise, it returns nothing, indicating that this row should be filtered out.
    """
    if fiscal_year_criteria != "":
        if project_row['fiscal_year'] == fiscal_year_criteria:
            return project_row
        else:
            return None
    else:
        return project_row

def start_date_filter(project_row, start_date_criteria):
    """
    Takes in project_rows from a .csv loop and checks the start_date field for a criterion.
    
    This is one of several filter functions that runs on individual project rows from the .csv
    dictionary object. This one takes in the "start_date" field from the filter_dict as
    start_date_criteria. It checks if the filter field is empty. If it is not, it then checks
    if the relevant contents of the .csv object matches the filter field. If the filter field is
    empty or matches the contents of the relevant field in the .csv project_row, it returns the 
    project_row. Otherwise, it returns nothing, indicating that this row should be filtered out.
    """
    if start_date_criteria != "":
        if project_row['start_date'] == start_date_criteria:
            return project_row
        else:
            return None
    else:
        return project_row

def area_filter(project_row, area_criteria):
    """
    Takes in project_rows from a .csv loop and checks the area field for a criterion.

    This is one of several filter functions that runs on individual project rows from the .csv
    dictionary object. This one takes in the "area" field from the filter_dict as
    area_criteria. It checks if the filter field is empty. If it is not, it then checks
    if the relevant contents of the .csv object matches the filter field. If the filter field is
    empty or matches the contents of the relevant field in the .csv project_row, it returns the 
    project_row. Otherwise, it returns nothing, indicating that this row should be filtered out.
    """
    if area_criteria != "":
        if project_row['area'] == area_criteria:
            return project_row
        else:
            return None
    else:
        return project_row

def asset_type_filter(project_row, asset_type_criteria):
    """
    Takes in project_rows from a .csv loop and checks the asset_type field for a criterion.
    
    This is one of several filter functions that runs on individual project rows from the .csv
    dictionary object. This one takes in the "asset_type" field from the filter_dict as
    asset_type_criteria. It checks if the filter field is empty. If it is not, it then checks
    if the relevant contents of the .csv object matches the filter field. If the filter field is
    empty or matches the contents of the relevant field in the .csv project_row, it returns the 
    project_row. Otherwise, it returns nothing, indicating that this row should be filtered out.
    """
    if asset_type_criteria != "":
        if project_row['asset_type'] == asset_type_criteria:
            return project_row
        else:
            return None
    else:
        return project_row

def planning_status_filter(project_row, planning_status_criteria):
    """
    Takes in project_rows from a .csv loop and checks the planning_status field for a criterion.
    
    This is one of several filter functions that runs on individual project rows from the .csv
    dictionary object. This one takes in the "planning_status" field from the filter_dict as
    planning_status_criteria. It checks if the filter field is empty. If it is not, it then checks
    if the relevant contents of the .csv object matches the filter field. If the filter field is
    empty or matches the contents of the relevant field in the .csv project_row, it returns the 
    project_row. Otherwise, it returns nothing, indicating that this row should be filtered out.
    """
    if planning_status_criteria != "":
        if project_row['status'] == planning_status_criteria:
            return project_row
        else:
            return None
    else:
        return project_row

def write_output(matching_list):
    """
    Takes in a list of things that match a filter and writes them to a newline-delimited text file.

    This function takes in the matching_list object that contains the id values of all objects
    that have met the criteria of the filter_dict. It writes each of these asset_id values to an 
    output.txt file with newline characters as delimiters.
    """
    with open ("output.txt", "w") as writer:
        for item in matching_list:
            writer.write(item + "\n")

def main():
    filter_dict = filter_reader()
    csv_reader(filter_dict)

if __name__ == "__main__":
    main()