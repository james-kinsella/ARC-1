import numpy as np
import json

path = r'..\data\training\7b7f7511.json'
json_data = json.loads(open(path).read())
black = 0
blue = 1

def solve(json_data):
    train = json_data['train']
    test = json_data['test']
    inputs = []
    for i in range(len(train)):
        inputs.append(train[i]['input'])
    
    for i in range(len(test)):
        inputs.append(test[i]['input'])
    
    for inp in inputs:
        solve_input(inp)
    
def solve_input(input):
    y_length = len(input)
    x_length = len(input[0])

    if y_length > x_length:
        for i in range(y_length // 2):
            input.pop()
    else:
        for i in range(y_length):
            for j in range(x_length // 2):
                input[i].pop()    
    output(input)

def output(inp):
    for i in inp:
        print(*i, sep=' ')
    print()
        
solve(json_data)