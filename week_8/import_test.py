# -*- coding: utf-8 -*-

import argparse
import urllib.request
from bs4 import BeautifulSoup

def get_input_file():
    """
    Takes in the name of an input file.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help=
        "Name of a newline-delimited list of categories.")
    args = parser.parse_args()
    input_file = args.input
    return input_file

def read_input_file(input_file):
    """
    Reads a newline-delimited list of categories into a python list object.
    """
    with open (input_file, "r") as categories_file:
        categories_list = categories_file.read().splitlines()
    return categories_list

def create_url(input_category):
    """
    Takes an input_category and uses .format() to insert it into a variable URL.
    """
    base_url = "https://brickset.com/sets/theme-{category}/year-2020"
    variable_url = base_url.format(category=input_category)
    variable_url = variable_url.replace(' ', '-')
    return variable_url

def get_html(url):
    """
    Uses urllib to request the full HTML text of a simple webpage.
    """
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        return response.read()

def find_titles(html):
    """
    Uses BeautifulSoup to find <img> objects and get their titles.
    """
    soup = BeautifulSoup(html, 'html.parser')
    sets = soup.find_all('img')
    for lego_set in sets:
        title = lego_set.get('title')
        if title:
            print(title)

def main():
    input_file = get_input_file()
    categories_list = read_input_file(input_file)
    for category in categories_list:
        url = create_url(category)
        print(category)
        html = get_html(url)
        find_titles(html)
        print("\n")

if __name__ == "__main__":
    main()