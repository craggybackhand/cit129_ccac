import numpy
import pandas
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', help="name of the input file")
    args = parser.parse_args()
    input_file = args.input_file
    return input_file

def read_csv(input_file):
    csv_object = pandas.read_csv(input_file)
    return csv_object

def north_versailles_counts(csv_object):
    north_versailles = csv_object[csv_object.city == 'North Versailles']
    nv_violations = north_versailles['description_new'].value_counts()
    nv_top_3 = nv_violations.iloc[0:3]
    return nv_top_3

def pittsburgh_counts(csv_object):
    pitt = csv_object[csv_object.city == 'Pittsburgh']
    pitt_violations = pitt['description_new'].value_counts()
    pitt_top_3 = pitt_violations.iloc[0:3]
    return pitt_top_3

def west_mifflin_counts(csv_object):
    west_mifflin = csv_object[csv_object.city == 'West Mifflin']
    wm_violations = west_mifflin['description_new'].value_counts()
    wm_top_3 = wm_violations.iloc[0:3]
    return wm_top_3

def print_output(municipality_name, top_3):
    print(
        f'Top 3 violations for {municipality_name}\n{str(top_3)}\n'
        )

input_file = parse_args()
csv_object = read_csv(input_file)
nv_top_3 = north_versailles_counts(csv_object)
pitt_top_3 = pittsburgh_counts(csv_object)
wm_top_3 = west_mifflin_counts(csv_object)
print_output('Pittsburgh', pitt_top_3)
print_output('North Versailles', nv_top_3)
print_output('West Mifflin', wm_top_3)