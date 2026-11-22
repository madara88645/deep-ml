
import numpy as np
def orthogonal_projection(v, L):
    """
    Compute the orthogonal projection of vector v onto line L.

    :param v: The vector to be projected
    :param L: The line vector defining the direction of projection
    :return: List representing the projection of v onto L
    """
    L_magsq = np.linalg.norm(L) ** 2
    L_v = np.dot(L,v)

    return list(np.array(L)*(L_v / L_magsq))
