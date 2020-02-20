import csv
import datetime
from collections import OrderedDict
from operator import itemgetter
from itertools import islice
        
def string_to_date(date_string):
    """
    Converts a date-formatted string into a datetime.date() object.

    Uses the datetime module's striptime function to convert a string representing a date value
    to a date() object. The string must have the specific formatting described. Returns the 
    formatted date object. 
    """
    formatted_date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    return formatted_date

def violation_counter(start_date, end_date):
    """
    Iterates over csv and counts violations in a date range, attaching them to a unique id.
    
    This function opens the target csv and uses csv.DictReader to read it into and OrderedDict
    object. It then iterates over each "row" in the csv, calls the string_to_date function to 
    convert the inspect_dt string field to a date value, and checks if the resulting date is 
    between a start_date and and an end_date. If it is, it assesses whether a violation's unique
    id is already present in the id_count dictionary and creates an entry if it's not. If it is
    already present, it increments the counter in the value for that id key. 
    """
    id_count = {}
    with open("inspection_data.csv", "r", newline='') as csv_reader:   
        reader = csv.DictReader(csv_reader)
        for row in reader:
            row_date = string_to_date(row['inspect_dt'])
            if (row_date >= start_date) and (row_date <= end_date):
                if (row['id'] not in id_count) and (row['facility_name'] != ''):
                    id_count[(row['id'])] = 1
                elif (row['facility_name'] != ''):
                    id_count[(row['id'])] += 1
    return id_count

def key_maker():
    """
    Iterates over csv to build a key mapping unique IDs to restaurant names.

    This function opens the target csv and uses csv.DictReader to read it into and OrderedDict
    object. It then iterates over each "row" in the csv and checks if the unique id of a given
    restaurant is in the restaurant_key dictionary. If it isn't and the facility_name field
    is not empty, it adds the id to the dictionary and includes the facility name as the value.
    """
    restaurant_key = {}
    with open("inspection_data.csv", "r", newline='') as csv_reader:
        reader = csv.DictReader(csv_reader) 
        for row in reader:
            if (row['id'] not in restaurant_key) and (row['facility_name'] != ''):
                restaurant_key[(row['id'])] = row['facility_name']
    return restaurant_key

def violation_mapper(id_count, restaurant_key):
    """
    Cross-references restaurant_key and id_count to map violations to restaurant names.

    This function imports the id_count and the restaurant_key dictionaries. It iterates through
    the ids in id_count, checking if the associated facility_name fields are already present in
    the violation_count dictionary. If they aren't, it adds them to the dictionary along with 
    the count of violations from the id_count dictionary.
    """
    violation_count = {}
    for id in id_count:
        if restaurant_key[id] not in violation_count:
            violation_count[(restaurant_key[id])] = id_count[id]
    return violation_count

def dict_sorter(unordered_dict):
    """
    Creates an OrderedDict object that is sorted in descending order by values in int format.

    Calls the collections.OrederedDict and operator.itemgetter libraries to take an unsorted
    dictionary and turn it into a sorted dictionary. The dictionary's integer values are used 
    and the resulting dictionary is sorted in descending order.
    """
    sorted_dict = OrderedDict(sorted(unordered_dict.items(), key=itemgetter(1), reverse=True))
    return sorted_dict

def top_ten_slicer(sorted_dict):
    """
    Users itertools.islice to slice the top ten items from an OrderedDict item.

    Calls the islice function from the itertools library against a sorted dictionary. The slicer
    value stores a slice of the first 10 entries in the dictionary, which is then turned into 
    and OrederedDict item and returned.
    """
    slicer = islice(sorted_dict.items(), 10)
    top_ten_dict = OrderedDict(slicer)
    return top_ten_dict

def main():
    """
    Iterates over inputted csv and calls other functions to return desired information.

    The start_date and end_date values are manually set in this function using the YYYY, MM, DD 
    format. After they are set, a series of functions are called to read the target csv and turn it
    into a sorted dictionary containing restaurant names and violation counts in the target date
    range. This sorted dictionary is sliced to return only the top ten results with the highest
    number of violations.
    """
    start_date = datetime.date(2016, 1, 1)
    end_date = datetime.date(201, 12, 31) 
    id_count = violation_counter(start_date, end_date)  
    restaurant_key = key_maker()
    violation_count = violation_mapper(id_count, restaurant_key)
    sorted_dict = dict_sorter(violation_count)
    top_ten_restaurants = top_ten_slicer(sorted_dict)
    print(top_ten_restaurants)

if __name__ == "__main__":
    main()