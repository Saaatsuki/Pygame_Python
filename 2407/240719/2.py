
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
    
    # bar = [ [random.randint(1, 100) for _ in range(matrix_col)]\
    #     for _ in range(matrix_row) ]
    
    return data_frame   

print(get_matrix(3))
print(get_matrix(3,2))
# get_matrix()
# get_matrix(1, 2)

#result = get_matrix()

#print(result) 