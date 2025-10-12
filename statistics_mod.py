def mean(vals):
    return sum(vals)/len(vals) if vals else 0.0
def variance(vals, sample=True):
    if not vals: return 0.0
    m = mean(vals)
    n = len(vals)
    s = sum((x-m)**2 for x in vals)
    return s/(n-1) if sample and n>1 else s/n
def describe(vals):
    return {"count": len(vals), "mean": mean(vals), "variance_sample": variance(vals, True)}
