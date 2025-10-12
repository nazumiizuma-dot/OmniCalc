from app.calculators.algebra import quadratic
from app.calculators.matrix_mod import inverse

def test_quadratic_real():
    out = quadratic(1,-3,2)
    assert 1.0 in out["roots"] or 2.0 in out["roots"]

def test_matrix_inverse():
    mat = [[4,7],[2,6]]
    out = inverse(mat)
    assert round(out["determinant"],3) == round((4*6-7*2),3)
