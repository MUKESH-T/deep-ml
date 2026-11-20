import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    arr = np.array(a)
    rows, columns = new_shape
    if rows * columns == arr.size:
        reshaped_matrix = arr.reshape(new_shape)
    else:
        reshaped_matrix = [] 
    return reshaped_matrix