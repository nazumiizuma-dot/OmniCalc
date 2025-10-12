import numpy as np
def inverse(mat):
    A = np.array(mat, dtype=float)
    inv = np.linalg.inv(A)
    return {"inverse": inv.tolist(), "determinant": float(np.linalg.det(A))}
