import numpy as np

def make_diagonal(x):
    # Your code here
    newx = np.zeros((len(x),len(x)))
    for j in range(len(newx)):
         newx[j][j] = x[j]
            
    return newx