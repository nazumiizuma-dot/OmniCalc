def kinematics(u: float, a: float, t: float):
    s = u * t + 0.5 * a * t * t
    v = u + a * t
    return {"displacement": s, "velocity": v}
