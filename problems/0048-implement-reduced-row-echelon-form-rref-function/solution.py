import numpy as np


def rref(matrix):
    A = np.array(matrix, dtype=float, copy=True)
    rows, cols = A.shape
    pivot_row = 0
    tol = 1e-10

    for col in range(cols):
        found_row = None

        for row in range(pivot_row, rows):
            if abs(A[row, col]) > tol:
                found_row = row
                break

        if found_row is None:
            continue

        A[[pivot_row, found_row]] = A[[found_row, pivot_row]]

        A[pivot_row] = A[pivot_row] / A[pivot_row, col]


            
        for target_row in range(rows):
            if target_row == pivot_row:
                continue
            factor = A[target_row, col] / A[pivot_row, col]
            A[target_row] = A[target_row] - factor * A[pivot_row]

        pivot_row += 1

    return A