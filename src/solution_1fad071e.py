import numpy as np
import json

path = r'..\data\training\1fad071e.json'
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
    blue_count = 0
    for y in range(len(input) - 1):
        for x in range(len(input[y]) - 1):
            if input[y][x] == blue:
                if input[y + 1][x + 1] == blue:
                    blue_count = blue_count + 1
                    x = x + 1
    output(blue_count)

def output(blue_count):
    output = []
    for i in range(5):
        if i < blue_count:
            output.append(blue)
        else:
            output.append(black)
    print(*output, sep=' ')
    print()

solve(json_data)