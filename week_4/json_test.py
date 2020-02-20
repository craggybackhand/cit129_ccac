# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:54:57 2020

@author: joel.whiteman
"""

import json


projects = {}
projects["group1"] = ['Dan', 'Eric1', 'Eric2', 'Eric3']
projects['group2'] = ('Zach', 'Taichi', 'Joel')
projects['unallocated'] = 452

# encode python object as JSON and write to a file
with open ('groups.json', 'w') as groupfile:
    # first argument is the object to be serialized, second is the filewriter object
    json.dump(projects, groupfile)

with open ('groups.json') as jsontest:
    groupkeywords = json.load(jsontest)

# opens json variable object and opens the key group1 and slices the list at its value 
print(groupkeywords['group1'][1:])