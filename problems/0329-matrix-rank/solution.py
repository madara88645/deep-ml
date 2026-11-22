import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    A = A.astype(float, copy=True)
    rows, cols = A.shape
    pivot_row = 0

    for col in range(cols):
        found_row = None
        for row in range(pivot_row,rows):    
            if abs(A[row, col]) > tol:
                found_row = row
                break
        if found_row == None:
            continue

        A[[pivot_row, found_row]] = A[[found_row, pivot_row]]

        for target_row in range(pivot_row + 1, rows):
            factor = A[target_row, col] / A[pivot_row, col]
            A[target_row] = A[target_row] - factor * A[pivot_row]
        pivot_row += 1

    return pivot_row

