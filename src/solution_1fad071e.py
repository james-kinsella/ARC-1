import common as comm
import itertools as itt
    
def solve(input):
    blue_count = 0
    y_length,x_length = comm.get_dimentions(input)
    for y,x in itt.product(range(y_length - 1), range(x_length - 1)):
        if input[y][x] == 1 and input[y + 1][x + 1] == 1:
            blue_count = blue_count + 1
    output_array = format_output(blue_count)
    comm.print_output(output_array)

def format_output(blue_count):
    output = []
    for i in range(5):
        if i < blue_count:
            output.append(1)
        else:
            output.append(0)
    return [output]
        
path = r'..\data\training\1fad071e.json'
json_data = comm.load_json(path)
inputs = comm.get_inputs(json_data)
comm.solve_all(solve, inputs)