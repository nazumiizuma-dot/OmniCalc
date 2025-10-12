UNIT_TABLE = {
    ("m","cm"): lambda v: v*100,
    ("cm","m"): lambda v: v/100,
    ("km","m"): lambda v: v*1000,
    ("m","km"): lambda v: v/1000,
    ("kg","g"): lambda v: v*1000,
    ("g","kg"): lambda v: v/1000,
}
def convert(value: float, from_unit: str, to_unit: str):
    key = (from_unit, to_unit)
    fn = UNIT_TABLE.get(key)
    if not fn:
        raise ValueError("Conversion not supported")
    return {"value": fn(value), "from": from_unit, "to": to_unit}
