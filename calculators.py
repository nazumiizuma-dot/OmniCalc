from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from app.calculators import arithmetic, algebra, calculus, statistics_mod, trigonometry, matrix_mod, transform_mod, physics_mod, converter, finance_mod, ai_helper

router = APIRouter()

class ExprIn(BaseModel):
    expr: str

@router.post("/arithmetic/add")
async def add_numbers(a: float, b: float):
    return {"result": arithmetic.add(a,b)}

@router.post("/algebra/quadratic")
async def solve_quadratic(a: float, b: float, c: float, steps: bool = False):
    return algebra.quadratic(a,b,c, steps=steps)

@router.post("/algebra/linear_system")
async def solve_linear_system(matrix: list, vector: list):
    return algebra.solve_linear_system(matrix, vector)

@router.post("/calculus/derivative")
async def derivative(expr: ExprIn, var: str = "x"):
    return calculus.derivative(expr.expr, var)

@router.post("/calculus/integrate_numeric")
async def integrate_numeric(expr: ExprIn, a: float = 0.0, b: float = 1.0):
    return calculus.integrate_numeric(expr.expr, a, b)

@router.post("/statistics/describe")
async def stats_describe(values: list):
    return statistics_mod.describe(values)

@router.post("/matrix/inverse")
async def matrix_inverse(mat: list):
    return matrix_mod.inverse(mat)

@router.post("/transform/dft")
async def transform_dft(values: list):
    return transform_mod.dft(values)

@router.post("/physics/kinematics")
async def physics_kinematics(u: float=0, a: float=0, t: float=0):
    return physics_mod.kinematics(u,a,t)

@router.post("/converter/unit")
async def convert_unit(value: float, from_unit: str = "m", to_unit: str = "cm"):
    return converter.convert(value, from_unit, to_unit)

@router.post("/finance/loan")
async def loan_calc(principal: float, annual_rate: float, years: int):
    return finance_mod.loan_payment(principal, annual_rate, years)

@router.post("/ai/help")
async def ai_help(q: ExprIn):
    return {"answer": ai_helper.ask(q.expr)}
