from sympy import sympify, Symbol, diff, lambdify
from scipy import integrate as sp_integrate

def derivative(expr: str, var: str = "x"):
    x = Symbol(var)
    try:
        f = sympify(expr)
        d = diff(f, x)
        return {"derivative": str(d)}
    except Exception as e:
        return {"error": str(e)}

def integrate_numeric(expr: str, a: float, b: float, var: str = "x"):
    x = Symbol(var)
    try:
        f = sympify(expr)
        f_l = lambdify(x, f, "numpy")
        res, err = sp_integrate.quad(f_l, a, b)
        return {"integral": float(res), "error_estimate": float(err)}
    except Exception as e:
        return {"error": str(e)}
