import math
from typing import List, Dict
import numpy as np

def quadratic(a: float, b: float, c: float, steps: bool=False) -> Dict:
    if a == 0:
        if b == 0:
            raise ValueError("a and b cannot both be zero")
        x = -c / b
        return {"roots": [x], "steps": ["Linear equation solved"] if steps else []}
    D = b*b - 4*a*c
    if D >= 0:
        r1 = (-b + math.sqrt(D)) / (2*a)
        r2 = (-b - math.sqrt(D)) / (2*a)
        return {"roots": [r1, r2], "discriminant": D}
    else:
        import cmath
        r1 = (-b + cmath.sqrt(D)) / (2*a)
        r2 = (-b - cmath.sqrt(D)) / (2*a)
        return {"roots": [str(r1), str(r2)], "discriminant": D}

def solve_linear_system(matrix: List[List[float]], vector: List[float]):
    A = np.array(matrix, dtype=float)
    b = np.array(vector, dtype=float)
    sol = np.linalg.solve(A, b)
    return {"solution": sol.tolist()}
