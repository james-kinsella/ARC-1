import json
import numpy as np

path = r'..\data\training\5ad4f10b.json'
json_data = json.loads(open(path).read())
black = 0

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
    colours = list(np.unique(input))
    colours.remove(0)

    if isPrimaryColour(input, colours[0]) == False:
        temp = colours[0]
        colours[0] = colours[1]
        colours[1] = temp
    sub_grid = find_boundries(input, colours[0])
    output(sub_grid, colours)
    
def isPrimaryColour(input, colour):
    y_length = len(input)
    x_length = len(input[0])
    
    run = 0
    prev = 0
    for y in range(y_length - 1):
        for x in range(x_length - 1):
            if input[y][x] == colour:
                if prev == colour:
                    run = run + 1
                    if(run == 3):
                        if input[y+1][x] == colour and input[y+2][x] == colour:
                            return True
                        else:
                            return False
                else:
                    prev = colour
                    run = run + 1
            else:
                if(prev == colour):
                        return False

def find_boundries(input, colour):
    y_length = len(input)
    x_length = len(input[0])

    for y in range(y_length):
        if(colour in input[y]):
            top = y
            break;
            
    for y in range(y_length):
        yval = y_length - (y+1)
        if(colour in input[yval]):
            bottom = yval
            break;
    t = np.transpose(input)
    for x in range(x_length):
        if(colour in t[x]):
            left = x
            break;
    for x in range(x_length):
        xval = x_length - (x+1)
        if(colour in t[xval]):
            right = xval
            break;

    return np.array(input)[top:bottom+1,left:right+1]


def output(inp, colours):
    step_size = len(inp) // 3    
    
    output_array = []
    for y in range(0, len(inp), step_size):
        yarr = []
        for x in range(0, len(inp), step_size):
            if inp[y][x] == colours[0]:
                yarr.append(colours[1])
            else:
                yarr.append(0)
        output_array.append(yarr)
    
    for i in output_array:
        print(*i, sep=' ')
    print()
    

solve(json_data)












