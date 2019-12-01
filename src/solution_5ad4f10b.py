import common as comm
import numpy as np

def solve(input):
    colours = list(np.unique(input))
    colours.remove(0)
    sort_colours(input, colours)
    sub_grid = find_boundries(input, colours[0])  
    return format_output(sub_grid, colours)
    
def sort_colours(input, colours):
    #the 'primary' colour is never present on any border
    #the 'secondary' colour is present on all borders
    if colours[0] in input[0]:
        tmp = colours[0]
        colours[0] = colours[1]
        colours[1] = tmp

def find_boundries(input, colour):
    y_length, x_length = comm.get_dimentions(input)

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


def format_output(inp, colours):
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
    return output_array


path = r'..\data\training\5ad4f10b.json'    
json_data = comm.load_json(path)
inputs = comm.get_inputs(json_data)

comm.solve_all(solve, inputs)



