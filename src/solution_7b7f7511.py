import common as comm
import itertools as itt
    
def solve(input):
    y_length,x_length = comm.get_dimentions(input)

    if y_length > x_length:
        for i in range(y_length // 2):
            input.pop()
    else:
        for y,x in itt.product(range(y_length), range(x_length // 2)):
            input[y].pop()    
    comm.print_output(input)
        
path = r'..\data\training\7b7f7511.json'
json_data = comm.load_json(path)
inputs = comm.get_inputs(json_data)
comm.solve_all(solve, inputs)