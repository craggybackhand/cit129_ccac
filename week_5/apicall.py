# -*- coding: utf-8 -*-
"""
Created on Mon Mar 9
@author: joel.whiteman
"""

import os
import requests
import json
import csv 

def read_year_file():
    """
    Reads a newline-delimited years.txt file and creates a list of all years in it.
    """
    with open ('years.txt', "r") as year_file:
        year_list = year_file.read().splitlines()
    return year_list

def year_iterator(year_list):
    """
    Iterates over a year_list and calls an API URL to build a dictionary of years and average parts.

    Builds an average_dict with years as keys and the average number of lego parts in sets from that
    year as values. For each year in year_list, the function creates an api_url composed of an 
    api_key and the year. It then calls get_json_by_year on that api_url and checks if the returned
    json includes any sets and if the year is valid. Finally, it populates average_dict with the
    year and the result of the api call.
    """
    average_dict = {}
    api_key = '15d39fe69a701f30c44cd700a1faa9a4'
    for year in year_list:
        api_url =('https://rebrickable.com/api/v3/lego/sets/?key=' + api_key + '&min_year=' + 
            year + '&max_year='  + year + '&page_size=1000')
        year_dict = get_json_by_year(api_url)
        if year_dict:
            if year_dict['count'] != 0:
                year_average_parts = get_average_parts_by_year(year_dict)
                average_dict[year] = year_average_parts
            else:
                average_dict[year] = "No Sets Found"
        else:
            average_dict[year] = "Invalid Year Value"
    return average_dict      

def get_json_by_year(api_url):
    """
    Calls an api_url, checks if the status is valid, and reads the returned json into a dict.

    Uses a structured api_url to make an api call. If the call returns a valid 200 status code, 
    uses the json.loads module to build a dictionary of all of the data returned for that year. If 
    the call returns an invalid status code, returns 'None'.
    """
    api_request = requests.get(api_url)
    if api_request.status_code == 200:
        year_dict = json.loads(api_request.text)
        return year_dict
    else:
        return None

def get_average_parts_by_year(year_dict):
    """
    Iterates over a year_dict to average the number of parts in the year's lego sets.

    Iterates over the list of lego set dictionaries stored in the year_dict key 'results.' Since 
    each list item is its own dictionary with the data regarding that particular set, the function
    looks at the 'num_parts' field in each set's dictionary. These are added to a running total of
    parts and the set_counter is incremented. Finally, the total_parts and set_counter variables
    are used to calculate an average number of parts in lego sets from that year. 
    """
    set_counter = 0
    total_parts = 0
    for lego_set in year_dict['results']:
        set_counter += 1
        total_parts += lego_set['num_parts']
    year_average_parts = (total_parts / set_counter)
    return str(year_average_parts)

def csv_writer(average_dict):
    """
    Writes a .csv with rows containing the years and average parts in that year's lego sets.

    Takes in the average_dict object and writes it to a .csv file. A header row is created, and
    then the year key and its value from average_dict are used to populate the rest of the rows
    in the .csv. 
    """
    with open('lego_averages.csv', 'w') as csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(['Year', 'Average Parts Per Set'])
        for year in average_dict:
            csv_write.writerow([year, average_dict[year]])

def main():
    year_list = read_year_file()
    average_dict = year_iterator(year_list)
    csv_writer(average_dict)

if __name__ == "__main__":
    main()