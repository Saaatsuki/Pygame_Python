
import random
def get_matrix(*args):
    
    if  not(1 <= len(args) <= 2):
        return None

    matrix_row = args[0]
    
    if len(args) == 1:
        matrix_col = args[0]
    else:
        matrix_col = args[1]    

    data_frame = {
        "num_row" : matrix_row,
        "num_col" : matrix_col,
        "data": [ [random.randint(1, 100) for _ in range(matrix_col)]\
         for _ in range(matrix_row) ]
    }
    
    data_frame['sum'] = lambda: sum([sum(row) for row in data_frame['data'] ])

    # bar = [ [random.randint(1, 100) for _ in range(matrix_col)]\
    #     for _ in range(matrix_row) ]
    
    return data_frame   

foo = dict()
foo['a'] = get_matrix(3,2)
foo['b'] = get_matrix(3,2)
foo['c'] = get_matrix(3,2)
foo['d'] = get_matrix(3,2)

result = sorted(foo.items(), key = lambda arg:arg[1]['sum']())

for item in result:
    print(item[1]['sum']())
