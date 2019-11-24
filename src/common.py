# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:46:12 2019

@author: jkinsella
"""

import json

def load_json(import_file):
    import_file = open(import_file)
    data = import_file.read()
    return json.loads(data)

def get_inputs(json_data):
    inputs = []
    for element in json_data:
        for pair in json_data[element]:
            inputs.append(pair['input'])
    return inputs

def solve_all(solve_funct, inputs):  
    for inp in inputs:
        solve_funct(inp)
        print()

def print_output(output):
    for i in output:
        print(*i, sep=' ')
        
def get_dimentions(inp):
    return len(inp),len(inp[0])
    